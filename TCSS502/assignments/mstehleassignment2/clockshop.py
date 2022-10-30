from clock import Clock


class ClockShop(Clock):
    """
    A simple ClockShop class to hold a list of Clock objects to allow for sorting, searching, retrieving,
    and printing the Clocks it contains.
        1) constructor __init__(): create a list to hold Clock objects
        2) __str__(self): builds a string containing each Clock object in string format.
           Each Clock object is separated from the others by a newline. Returns the string.
        3) fill_clock_shop(self, list_of_times): accepts a list of string times formatted hh:mm:ss, then
           creates Clock objects for each time and adds it to the list of clocks. Returns the list.
        4) sort_clocks(self): sorts the list of clocks and returns the sorted list. Since we had not yet
           covered sort methods in class, we were permitted to use Python's built-in sort method.
        5) find_clock(self, a_clock): accepts a Clock object and checks to see if it exists in the list.
           Returns the index of where the object is found if it exists, and returns -1 if it does not exist.
        6) get_clock(self, index): accepts an integer index and pulls the appropriate Clock from the list.
           If the index falls within the list, returns the Clock found.
        7) set_clock(self, a_clock, index): accepts a Clock object and an index and places the new Clock
           at the specified index in the list. Does not return any value.
    """
    def __init__(self):
        self.__clock_list = []

    def __str__(self):
        clock_string = ''

        for i in range(0, len(self.__clock_list)):
            clock_string += f'{self.__clock_list[i].hours}:{self.__clock_list[i].minutes}:{self.__clock_list[i].seconds}\n'

        return clock_string

    def fill_clock_shop(self, list_of_times):
        for i in range(0, len(list_of_times)):
            new_Clock = Clock()
            counter = 0
            time_digits = ''

            for j in range(0, len(list_of_times[i])):

                if list_of_times[i][j] == ':':
                    time_digits = ''
                    counter += 1
                    continue
                else:
                    time_digits += list_of_times[i][j]

                    if counter == 0:
                        new_Clock.set_hour(int(time_digits))
                    elif counter == 1:
                        new_Clock.set_minute(int(time_digits))
                    elif counter == 2:
                        new_Clock.set_second(int(time_digits))

            self.__clock_list.append(new_Clock)

        return self.__clock_list

    def sort_clocks(self):
        self.__clock_list.sort()
        return self.__clock_list

    def find_clock(self, a_clock):
        for i in range(0, len(self.__clock_list)):
            if a_clock == self.__clock_list[i]:
                return i

        return -1

    def get_clock(self, index):
        if not self.__clock_list:
            raise ValueError('List is empty!')
        elif 0 <= index < len(self.__clock_list):
            return self.__clock_list[index]
        else:
            raise ValueError('That index does not exist in this list of clocks!')

    def set_clock(self, a_clock, index):
        if not self.__clock_list:
            raise ValueError('List is empty!')
        if 0 <= index < len(self.__clock_list):
            self.__clock_list[index] = a_clock
        else:
            raise IndexError('That index does not exist in this list of clocks!')