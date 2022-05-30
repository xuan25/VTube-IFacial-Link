import threading

from livelinkface.pylivelinkface import PyLiveLinkFace


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
        data = PyLiveLinkFace()
        return data
