# Python-Notification-Server

## 🧰 Commands

### 📣

To display a list of the notification server's history, send a notification with the application name set as shw-msg. Additionally, you can query a specific notification by providing its ID using the -r option.

```zsh
notify-send '' -a 'shw-msg'
notify-send '' -a 'shw-msg' -r [notification_id]
```

### 🗑️

The rm-msg command is used to remove a specific notification from the notification server. This command allows users to clear or dismiss notifications based on their unique identifier, known as the notification ID.

```zsh
notify-send '' -a 'rm-msg' -r [notification_id]
```
