from clock import Clock


class ClockShop(Clock):
    """
    Comment go here weeee
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

                # if j == len(list_of_times[i]) - 1:
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