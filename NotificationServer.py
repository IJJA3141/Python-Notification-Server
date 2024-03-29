#!/bin/python

import dbus.service
import threading
import os.path
import dbus
import time


def wait(notification_server, timeout, notification_id):
    time.sleep(timeout / 1000)
    notification_server.remove_notification(notification_id, 1)

    return


class Notification:
    def __init__(self, app_name, app_icon, summary, body):
        self.app_name = app_name
        self.app_icon = app_icon
        self.summary = summary
        self.body = body


class NotificationServer(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName(
            "org.freedesktop.Notifications", bus=dbus.SessionBus()
        )
        dbus.service.Object.__init__(self, bus_name, "/org/freedesktop/Notifications")

        self.notifications = {}
        self.history = {}
        self.default_timeout = 5000
        self.id = 0
        self.path = "./logs.txt"

    # Signals
    @dbus.service.signal("org.freedesktop.notifications", signature="uu")
    def NotificationClosed(self, notification_id, reason):
        return

    @dbus.service.signal("org.freedesktop.notifications", signature="us")
    def ActionInvoked(self, notification_id, action_key):
        return

    # Methods that just need to be here
    @dbus.service.method("org.freedesktop.Notifications", in_signature="u")
    def CloseNotification(self, notification_id):
        self.remove_notification(notification_id, 3)
        return

    @dbus.service.method("org.freedesktop.Notifications", out_signature="ssss")
    def GetServerInformation(self):
        return ("Notification Server", "IJJA3141", "1.0", "1.2")

    @dbus.service.method("org.freedesktop.Notifications", out_signature="as")
    def GetCapabilities(self):
        return ("actions", "body", "body-hyprlinks", "icon-static")

    @dbus.service.method(
        "org.freedesktop.Notifications", in_signature="susssasa{sv}i", out_signature="u"
    )
    def Notify(
        self,
        app_name,
        replaces_id,
        app_icon,
        summary,
        body,
        actions,
        hints,
        timeout,
    ):
        if app_name == "rm-msg":
            if replaces_id:
                self.ActionInvoked(replaces_id, "activate")
                self.remove_notification(replaces_id, 2)
            return 0
        if app_name == "shw-msg":
            self.print_hist(replaces_id)
            return 0

        if replaces_id != 0:
            self.remove_notification(replaces_id, 1)

        self.id += 1
        self.notifications[self.id] = Notification(app_name, app_icon, summary, body)
        self.history[self.id] = Notification(app_name, app_icon, summary, body)

        if not os.path.isfile(self.path):
            open(self.path, "x")
        f = open(self.path, "a")

        f.write(
            f"""[{self.id}]\nAppname: {app_name or ''}\nSummary: {summary or ''}\nBody: {body or ''}\n\n"""
        )

        f.close()

        self.print_state()

        if timeout == -1:
            timer_thread = threading.Thread(
                target=wait, args=(self, self.default_timeout, self.id)
            )
            timer_thread.start()
        elif timeout != 0:
            timer_thread = threading.Thread(target=wait, args=(self, timeout, self.id))
            timer_thread.start()

        return self.id

    def remove_notification(self, notification_id, reason):
        if self.notifications.get(notification_id):
            self.notifications.pop(notification_id)
            self.print_state()
            self.NotificationClosed(notification_id, reason)

        return

    def print_state(self):
        for notification_key in self.notifications:
            print("name", self.notifications[notification_key].app_name)
            print("icon", self.notifications[notification_key].app_icon)
            print("summary", self.notifications[notification_key].summary)
            print("body", self.notifications[notification_key].body)

        return

    def print_hist(self, replaces_id):
        if replaces_id:
            print("id", replaces_id)
            print("name", self.history[replaces_id].app_name)
            print("icon", self.history[replaces_id].app_icon)
            print("summary", self.history[replaces_id].summary)
            print("body", self.history[replaces_id].body)
        else:
            for notification_key in self.history:
                print("id", notification_key)
                print("name", self.history[notification_key].app_name)
                print("icon", self.history[notification_key].app_icon)
                print("summary", self.history[notification_key].summary)
                print("body", self.history[notification_key].body)

        return
