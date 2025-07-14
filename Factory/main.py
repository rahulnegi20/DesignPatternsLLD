from abc import ABC, abstractmethod

#Interface :  an interface defines a contract of what methods a class must implement, without specifying how those methods are implemented.s

class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass



# NOTIFICATION CLASSES

class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending email notification: {message}")


class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")


class PushNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Sending push notification: {message}")

"""
Each concrete class implements the Notification interface and has its own logic for sending the notification.
"""


class NotificationFactory:
    @staticmethod
    def create_notification(channel_type):
        if channel_type == "email":
            return EmailNotification()
        elif channel_type == "sms":
            return SMSNotification()
        elif channel_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification channel: {channel_type}")



# USAGE

def send_notification(channel_type, message):
    try:
        notification = NotificationFactory.create_notification(channel_type)
        notification.send(message)
    except ValueError as e:
        print(e)

# Test the factory with different notification types
send_notification("email", "Hello via Email!")
# Output: "Sending email notification with message: Hello via Email!"

send_notification("sms", "Hello via SMS!")
# Output: "Sending SMS notification with message: Hello via SMS!"

send_notification("push", "Hello via Push!")
# Output: "Sending push notification with message: Hello via Push!"

send_notification("fax", "Hello via Fax!")  # This will raise an error
# Output: "Unknown notification channel: fax"


"""

Why the Factory Pattern Works Well Here?

    Scalability: Adding a new notification type (like FaxNotification) is easy. Just create a FaxNotification class implementing Notification and add it to the factory. The existing code doesn’t change.
    Encapsulation of Creation Logic: The client doesn’t need to know which specific class to instantiate. It simply specifies the type, and the factory handles the rest.
    Decoupling: The client code (send_notification) doesn’t depend on the concrete classes (EmailNotification, SMSNotification, PushNotification). It only interacts with the Notification interface, making the code more modular.

This approach is commonly used in systems where multiple types of objects need to be created dynamically, based on runtime conditions, and each type follows a similar structure but has different implementations.
"""