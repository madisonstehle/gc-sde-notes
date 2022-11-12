from observable import Observable

class EyeOfSauron(Observable):
    """
     EyeOfSauron Class
     A class containing the structure for the EyeOfSauron.
     Keeps track of the number of good guys (hobbits, dwarves, elves, humans)
     Includes init, setEnemies methods
     Inherits from Observable class
    """

    def __init__(self):
        """
        constructor __init__(self) that creates an EyeOfSauron object and a data structure to hold the good guy counts
            inherits from Observable class as super()
            parameters: None
            return: None
        """
        super().__init__()
        self.good_guys = {"dwarf_count": 0, "human_count": 0, "hobbit_count": 0, "elf_count": 0}


    def setEnemies(self, hobbit_count, dwarf_count, elf_count, human_count):
        """
        setEnemies(self, hobbit_count, dwarf_count, elf_count, human_count) that checks that the number
        of each good guy is the same as what was stored previously. If it changed, updates the stored value
        and notifies all observers
            parameters: hobbit_count, dwarf_count, elf_count, human_count
            return: None
        """
        change_tracker = False

        for key in self.good_guys:
            if key == 'dwarf_count':
                if self.good_guys[key] != dwarf_count:
                    self.good_guys['dwarf_count'] = dwarf_count
                    change_tracker = True
            if key == 'human_count':
                if self.good_guys[key] != human_count:
                    self.good_guys['human_count'] = human_count
                    change_tracker = True
            if key == 'hobbit_count':
                if self.good_guys[key] != hobbit_count:
                    self.good_guys['hobbit_count'] = hobbit_count
                    change_tracker = True
            if key == 'elf_count':
                if self.good_guys[key] != elf_count:
                    self.good_guys['elf_count'] = elf_count
                    change_tracker = True

        if change_tracker:
            self.notify_observers(self.good_guys)
