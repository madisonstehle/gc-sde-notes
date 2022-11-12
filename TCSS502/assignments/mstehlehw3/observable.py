"""
Extra Credit for has_changed, set_changed, clear_changed to keep track of whether or not the observable has changed (+5)
"""

class Observable:
    """
    Observable Class
    A class containing the structure for the observable.
    Includes init, notify_observers, add_observer, remove_observer methods
    """

    def __init__(self):
        """
        constructor __init__(self) that creates an Observable object and creates a data structure to hold the observers
            parameters: None
            return: None
        """
        self.observers = []


    def add_observer(self, observer):
        """
        add_observer(self, observer) that adds an observer to the data structure
            parameters: observer
            return: None
        """
        self.observers.append(observer)


    def remove_observer(self, observer):
        """
        remove_observer(self, observer) that removes an observer from the data structure
            parameters: observer
            return: None
        """
        self.observers.remove(observer)


    def notify_observers(self, notification_data):
        """
        notify_observers(self, notification_data) If the observable has changed, notify all observers
            parameters: notification_data
            return: None
        """
        if self.observers:
            for i in range(0, len(self.observers)):
                self.observers[i].notify(notification_data)


    ### EXTRA CREDIT METHODS ###
    
    def clear_changed(self):
        pass

    def set_changed(self):
        pass

    def has_changed(self):
        pass
