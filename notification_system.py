from abc import ABC, abstractmethod

class INotification(ABC):
    @abstractmethod
    def notify(self, msg): pass

class Email(INotification):
    def notify(self, msg):
        print(f"{msg} is sent via email")

class SMS(INotification):
    def notify(self, msg):
        print(f"{msg} is sent via SMS")

class NotificationFactory:
    def __init__(self):
        self._creators = {
            "email": Email,
            "sms": SMS
        }

    def create(self, type) -> INotification:
        cls = self._creators.get(type)
        if not cls:
            raise ValueError(f"Unknown notification type: {type}")
        return cls()

    def register(self, name, class_name):
        self._creators[name] = class_name

class NotificationService:
    def __init__(self, factory: NotificationFactory):
        self.factory = factory

    def send(self, type, msg):
        notificatoin = self.factory.create(type)
        notificatoin.notify(msg)

service = NotificationService(NotificationFactory())
service.send("email", "hello")