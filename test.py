from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import NotificationServer

# Not needed, just for the examlpe
import threading
import time
import os


DBusGMainLoop(set_as_default=True)


def wait_and_clear():
    time.sleep(5)
    os.system("clear")
    return


def print_example(self):
    os.system("clear")
    for notification_key in self.notifications:
        print("key", notification_key)

    timer_thread = threading.Thread(target=wait_and_clear)
    timer_thread.start()


if __name__ == "__main__":
    server = NotificationServer.NotificationServer()

    # You can modify the default timeout like this
    server.default_timeout = 2000

    # And to modify the printing behavior use this
    server.print_state = print_example.__get__(server)

    mainloop = GLib.MainLoop()
    mainloop.run()
