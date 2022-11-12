"""
Extra Credit for declaring as an Abstract Base Class (+2)
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Observer Class
    An abstract base class containing the structure for the observer.
    Includes a notify/update method and an init
    """

    @abstractmethod
    def __init__(self):
        """
        constructor __init__() abstract base class that creates an Observer object
            parameters: None
            return: None
        """
        pass

    def notify(self, notification_data):
        """
        notify(self) abstract base class method to notify of updates
            parameters: notification_data
            return: None
        """
        pass
