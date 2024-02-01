# Python Notification Server

This project provides a customizable notification server implemented in Python, allowing users to manage and interact with notifications in their desktop environment. The server is designed to handle various notification-related tasks, such as displaying notifications, tracking notification history, and providing commands for interacting with notifications.

## ⚡️ Features:

- **Notification Display:** The server supports the display of notifications with essential details such as application name, icon, summary, and body.
- **Notification History:** Users can query the notification server to retrieve a list of past notifications, facilitating a quick review of recent activities.

- **Notification Removal:** The server allowing users to remove specific notifications by providing their unique IDs.

- **Action Handling:** Notifications may include actions, and the server can respond to these actions, providing a versatile user interaction experience.

- **Notification Logging:** The server features a comprehensive notification logging system that records all notifications sent to the server. This information is stored in a log file, allowing users to maintain a detailed record of notification activities over time.

## 📦 Installation

- Clone the repository.
- If required, install the following dependencies: dbus-python, libnotify.

## ⚙️ Customization

- Explore the code to customize the server behavior to suit your preferences.
- Adapt the notification handling logic according to your needs.

**Customization exemple:**
[test.py](https://github.com/IJJA3141/Python-Notification-Server/blob/main/test.py)

```python
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
```

## 🧰 Usage:

- Run the Python Notification Server script.
- Interact with the server using commands like `shw-msg` and `rm-msg`.

### Commands

- **📣 Show Notification Server History:** Use the `shw-msg` command to display a list of the notification server's history. You can also query a specific notification by providing its ID.

  ```zsh
  notify-send '' -a 'shw-msg'
  notify-send '' -a 'shw-msg' -r [notification_id]
  ```

###

- **🗑️ Remove Notification:** Utilize the `rm-msg` command to remove a specific notification from the server by providing its ID. (It won't be removed from the history)

  ```zsh
  notify-send '' -a 'rm-msg' -r [notification_id]
  ```

## 🎭 Motivations

I use a modified version of this server for my self that can be found in my [dotfiles](https://github.com/IJJA3141/.config/blob/linux/eww/scripts/notification.py) and could't find enithing similar so if it can be usefull to someone it's here
