import sys

import wx

from commandline import CommandLine
from frames import ParamsFrame
from models import CapturedData
from threads import CaptureThread, PluginThread


def main(udp_address):

    capture_data = CapturedData()

    client_thread = CaptureThread(capture_data, udp_address)
    client_thread.start()

    plugin_thread = PluginThread(capture_data)
    plugin_thread.start()

    app = wx.App()
    main_frame = ParamsFrame(capture_data)
    main_frame.Show(True)
    app.MainLoop()

    plugin_thread.should_terminate = True
    plugin_thread.join()

    client_thread.should_terminate = True
    client_thread.join()


if __name__ == "__main__":

    config = CommandLine()
    if config.exit:
        sys.exit(0)

    main(config.udp_address)
