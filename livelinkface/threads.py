
import asyncio
import socket
import threading

import websockets
from livelinkface.model import CapturedData
from livelinkface.utils import build_params_dict

import vtube

class CaptureThread(threading.Thread):

    def __init__(self, capture_data: CapturedData):
        super().__init__()
        self.capture_data = capture_data
        self.should_terminate = False

    def run(self):
        from livelinkface.pylivelinkface import PyLiveLinkFace, FaceBlendShape

        UDP_PORT = 11111

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # open a UDP socket on all available interfaces with the given port
        s.bind(("", UDP_PORT)) 
        while not self.should_terminate: 
            data, addr = s.recvfrom(1024) 
            # decode the bytes data into a PyLiveLinkFace object
            success, live_link_face = PyLiveLinkFace.decode(data)
            if success:
                self.capture_data.write_data(live_link_face)
                # # get the blendshape value for the HeadPitch and print it
                # pitch = live_link_face.get_blendshape(FaceBlendShape.HeadPitch)
                # print(live_link_face.name, pitch)       
                # pass

        s.close()

class PluginThread(threading.Thread):

    def __init__(self, capture_data: CapturedData):
        super().__init__()
        self.capture_data = capture_data
        self.should_terminate = False

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop.run_until_complete(self.run_loop())
        loop.close()

    async def run_loop(self):
        websocket = await websockets.connect('ws://127.0.0.1:8001')

        await vtube.init(websocket)

        while not self.should_terminate:
            raw_data = self.capture_data.read_data()
            parameter_values = build_params_dict(raw_data)
            pack = await vtube.inject_params(websocket, parameter_values)
        await websocket.close()
