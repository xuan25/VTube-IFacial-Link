
from time import sleep
from livelinkface.model import CapturedData
from livelinkface.threads import CaptureThread, PluginThread


def main():

    capture_data = CapturedData()

    client_thread = CaptureThread(capture_data)
    client_thread.start()

    plugin_thread = PluginThread(capture_data)
    plugin_thread.start()

    while True:
        sleep(1)

    plugin_thread.should_terminate = True
    plugin_thread.join()

    client_thread.should_terminate = True
    client_thread.join()


if __name__ == "__main__":
    main()
