import threading

import ifacial


class CapturedData:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = self.create_default_data()

    def write_data(self, data):
        self.lock.acquire()
        self.data = data
        self.lock.release()

    def read_data(self):
        self.lock.acquire()
        output = self.data
        self.lock.release()
        return output

    @staticmethod
    def create_default_data():
        data = {}

        for blendshape_name in ifacial.BLENDSHAPE_NAMES:
            data[blendshape_name] = 0.0

        data[ifacial.HEAD_ROTATION_X] = 0.0
        data[ifacial.HEAD_ROTATION_Y] = 0.0
        data[ifacial.HEAD_ROTATION_Z] = 0.0

        data[ifacial.HEAD_POSITION_X] = 0.0
        data[ifacial.HEAD_POSITION_Y] = 0.0
        data[ifacial.HEAD_POSITION_Z] = 0.0

        data[ifacial.LEFT_EYE_ROTATION_X] = 0.0
        data[ifacial.LEFT_EYE_ROTATION_Y] = 0.0
        data[ifacial.LEFT_EYE_ROTATION_Z] = 0.0

        data[ifacial.RIGHT_EYE_ROTATION_X] = 0.0
        data[ifacial.RIGHT_EYE_ROTATION_Y] = 0.0
        data[ifacial.RIGHT_EYE_ROTATION_Z] = 0.0

        return data
