import argparse

from ifacial.models import CapturedData
from ifacial.threads import CaptureThread, PluginThread


def main(udp_address, gui):

    capture_data = CapturedData()

    client_thread = CaptureThread(capture_data, udp_address)
    client_thread.start()

    plugin_thread = PluginThread(capture_data)
    plugin_thread.start()

    if gui:
        import wx
        from ifacial.frames import ParamsFrame
        app = wx.App()
        main_frame = ParamsFrame(capture_data)
        main_frame.Show(True)
        app.MainLoop()
    else:
        try:
            while(True):
                import time
                time.sleep(1)
        except KeyboardInterrupt:
            print('shutting down')


    plugin_thread.should_terminate = True
    plugin_thread.join()

    client_thread.should_terminate = True
    client_thread.join()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                    prog = 'VTube-IFacial-Link',
                    description = 'A *VTube Studio* plugin that bridging facial tracking from *iFacialMocap* (IOS), enabling full apple ARKit facial tracking features.')

    parser.add_argument('-c', '--connect', required=True, help='the IP address of capturing device to connect. Please set with the address shown in the iFacialMocap')
    parser.add_argument('-b', '--no-gui', action='store_true', default=False, help='Flag that run the program without GUI')
    args = parser.parse_args()

    main(args.connect, (not args.no_gui))
