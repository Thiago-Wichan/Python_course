from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self):
        ...

class EmailNotification (Notification):
    def send(self):
        print ('Email -> sending...', self.message)
        return True
    
class SMSNotification (Notification):
    def send(self):
        print ('SMS -> sending...', self.message)
        return False

def notify(notification: Notification):
    send_notification = notification.send

    if send_notification:
        print('Notification sended')
    else:
        print('Notification not send')

notification_email = EmailNotification('email testing')

notify(notification_email)

notification_sms = SMSNotification('SMS testing')

notify(notification_sms)

