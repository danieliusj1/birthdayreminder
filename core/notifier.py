from abc import ABC, abstractmethod
from plyer import notification

class Notifier(ABC):
  #an example of an abstract method using the abc module - it defines a 'send' interface
    @abstractmethod
    def send(self, title: str, message: str):
        pass

class NotificationService(Notifier):
  #an example of inheritance, since this class inherits the send method from the Notifier class
    _instance = None

    def __new__(cls):
      #singleton design pattern - ensures only one instance of NotificationService exists and is used to centralize the whole birthday notification logic
        if cls._instance is None:
            cls._instance = super(NotificationService, cls).__new__(cls)
        return cls._instance

    def send(self, title: str, message: str):
        #polymorphism example - class inherits from Notifier and overrides the send method
        notification.notify(
            title=title,
            message=message,
            timeout=10
        )
