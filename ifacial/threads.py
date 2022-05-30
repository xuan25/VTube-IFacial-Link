

import asyncio
import socket
import threading

import websockets

import ifacial
import vtube
from ifacial.models import CapturedData
from ifacial.utils import build_params_dict


class CaptureThread(threading.Thread):
    def __init__(self, capture_data: CapturedData, udp_address: str):
        super().__init__()
        self.capture_data = capture_data
        self.should_terminate = False
        self.udp_address = udp_address
        self.port = 49983

    def run(self):
        self.udp_listener_loop()

    def udp_listener_loop(self):
        udpClntSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = "iFacialMocap_sahuasouryya9218sauhuiayeta91555dy3719"
        data = data.encode('utf-8')
        udpClntSock.sendto(data, (self.udp_address, self.port))

        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind(("", 49983))
        server.settimeout(0.05)

        while not self.should_terminate:
            try:
                messages, address = server.recvfrom(8192)
                udp_msg = messages.decode('utf-8')
                data = self.convert_from_raw_data(udp_msg)
                self.capture_data.write_data(data)
            except:
                pass

    @staticmethod
    def convert_from_raw_data(raw_data):
        params_dict = {}
        param_strs = raw_data.strip('|').split('|')
        for param_str in param_strs:
            if('#' in param_str):
                key_val_str = param_str.split('#')
                key = key_val_str[0]
                vals = []
                val_strs = key_val_str[1].split(',')
                for val_str in val_strs:
                    vals.append(float(val_str))
                params_dict[key] = vals
            else:
                key_val_str = param_str.split('-')
                key = key_val_str[0]
                val = float(key_val_str[1]) / 100
                params_dict[key] = val

        data = {}

        for blendshape_name in ifacial.BLENDSHAPE_NAMES:
            data[blendshape_name] = params_dict[blendshape_name]

        data[ifacial.HEAD_ROTATION_X] = params_dict["=head"][0]
        data[ifacial.HEAD_ROTATION_Y] = params_dict["=head"][1]
        data[ifacial.HEAD_ROTATION_Z] = params_dict["=head"][2]
        data[ifacial.HEAD_POSITION_X] = params_dict["=head"][3]
        data[ifacial.HEAD_POSITION_Y] = params_dict["=head"][4]
        data[ifacial.HEAD_POSITION_Z] = params_dict["=head"][5]

        data[ifacial.RIGHT_EYE_ROTATION_X] = params_dict["rightEye"][0]
        data[ifacial.RIGHT_EYE_ROTATION_Y] = params_dict["rightEye"][1]
        data[ifacial.RIGHT_EYE_ROTATION_Z] = params_dict["rightEye"][2]

        data[ifacial.LEFT_EYE_ROTATION_X] = params_dict["leftEye"][0]
        data[ifacial.LEFT_EYE_ROTATION_Y] = params_dict["leftEye"][1]
        data[ifacial.LEFT_EYE_ROTATION_Z] = params_dict["leftEye"][2]

        return data

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
            ifacial_data = self.capture_data.read_data()
            parameter_values = build_params_dict(ifacial_data)
            pack = await vtube.inject_params(websocket, parameter_values)
        await websocket.close()
