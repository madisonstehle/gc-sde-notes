from observer import Observer

class BadGuy(Observer):
    """
     BadGuy Class
     A class containing the structure for a BadGuy.
     Registers current BadGuy (self) with the eye.
     Includes init, notify, defeated methods
     Inherits from Observer class
    """

    def __init__(self, eye, name):
        """
        constructor __init__(self, eye, name) that creates an BadGuy object with a name and registers the new BadGuy with eye
            inherits from Observer class as super()
            parameters: eye, name
            return: None
        """
        super().__init__()
        self.__eye = eye
        self.__name = name
        self.__eye.add_observer(self)


    def notify(self, notification_data):
        """
        notify(self, notification_data) that prints the new good guy data when notified by the Observable
            parameters: notification_data
            return: None
        """
        dwarf_num = notification_data['dwarf_count']
        human_num = notification_data['human_count']
        elf_num = notification_data['elf_count']
        hobbit_num = notification_data['hobbit_count']
        print(f'Change Spotted by {self.__name}:')
        print(f'There are {dwarf_num} dwarves, {human_num} humans, {elf_num} elves, and {hobbit_num} hobbits!')


    def defeated(self):
        """
        defeated(self) that removes current BadGuy (self) from the list of observers
            parameters: None
            return: None
        """
        print(f"{self.__name} was defeated!")
        self.__eye.remove_observer(self)


