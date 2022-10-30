from datetime import datetime


class Clock:
    """
    A simple Clock class to represent time in hours, minutes, and seconds.
    The type of time it represents is in military time (hours are from 0 to 23,
    with 0 representing midnight and 23 representing 11pm).
        1) constructor __init__() create a Clock object and specify the starting hour, minute, and second via integer parameters.
          it defaults to 00:00:00 (hours, minutes, seconds) (12am) if no values are specified at creation
        2) __str__(self): get the current time in String format -- the object will return a String
          with the hours, minutes and seconds as follows: hh:mm:ss (ex: 9:49:59)
        3) __repr__(self): get the current time in String format -- the object will return a String
          with the hours, minutes and seconds as follows: hh:mm:ss (ex: 9:49:59)
        4) hour(self): the object will report as follows: hh
          (ex: 18 -- which means it is 6pm) -- the value returned should be the hour
        5) minute(self): the object will report as follows: mm
          (ex: 56) -- the value returned should be the minute
        6) second(self): the object will report as follows: ss
          (ex: 29) -- the value returned should be the seconds
        7) set_hour(self, new_hour): accepts a number from 0 through 23 and sets the clock hour.
           Does not return any value
        8) set_minute(self, new_minute): accepts a number from 0 through 59 and sets the clock minute.
           Does not return any value
        9) set_second(self, new_second): accepts a number from 0 through 59 and sets the clock second.
           Does not return any value
        10) advance_hour(self, amount_to_advance): advances the current hour. Accepts a number 0 or greater
            Does not return any value
        11) advance_minute(self, amount_to_advance): advances the current minute and updates hour if necessary.
            Accepts a number 0 or greater. Does not return any value
        12) set_to_current_time(self): sets the clock time to the current time based on the system time.
            Does not return any value
        13) __eq__(self, other): compares against another Clock object for equality in hours, minutes, and seconds.
            Returns True or False
        14) __lt__(self, other): compares against another Clock object for if current clock’s time is before other clock.
            Returns True or False
        15) __gt__(self, other): compares against another Clock object for if current clock’s time is after other clock.
            Returns True or False
    """
    def __init__(self, hours=00, minutes=00, seconds=00):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def __repr__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def hour(self):
        return self.hours

    def minute(self):
        return self.minutes

    def second(self):
        return self.seconds

    def set_hour(self, new_hour):
        if 0 <= new_hour <= 23:
            self.hours = new_hour
        else:
            raise ValueError('Hour must be an integer between 00 and 23')

    def set_minute(self, new_minutes):
        if 0 <= new_minutes <= 59:
            self.minutes = new_minutes
        else:
            raise ValueError('Minute must be an integer between 00 and 59')

    def set_second(self, new_seconds):
        if 0 <= new_seconds <= 59:
            self.seconds = new_seconds
        else:
            raise ValueError('Second must be an integer between 00 and 59')

    def advance_hour(self, amount_to_advance):
        if (self.hours + amount_to_advance) < 0:
            raise ValueError('Hour cannot be less than 0!')
        elif 0 <= (self.hours + amount_to_advance) <= 23:
            self.hours += amount_to_advance
        elif (self.hours + amount_to_advance) > 23:
            placeholder_hour = self.hours + amount_to_advance

            while placeholder_hour > 23:
                placeholder_hour -= 24

            self.hours = placeholder_hour

    def advance_minute(self, amount_to_advance):
        if (self.minutes + amount_to_advance) < 0:
            raise ValueError('Minutes cannot be less than 0!')
        elif 0 <= (self.minutes + amount_to_advance) <= 59:
            self.minutes += amount_to_advance
        elif (self.minutes + amount_to_advance) > 59:
            placeholder_minutes = self.minutes + amount_to_advance

            while placeholder_minutes > 59:
                placeholder_minutes -= 60
                if self.hours + 1 == 24:
                    self.hours = 0
                else:
                    self.hours += 1

            self.minutes = placeholder_minutes

    def set_to_current_time(self):
        hr_str = datetime.now().strftime('%H')
        self.set_hour(int(hr_str))

        mi_str = datetime.now().strftime('%M')
        self.set_minute(int(mi_str))

        sec_str = datetime.now().strftime('%S')
        self.set_second(int(sec_str))

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise TypeError("That is not a Clock!")
            return

        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise TypeError("That is not a Clock!")
            return

        if self.hours < other.hours:
            return True
        elif self.hours == other.hours and self.minutes < other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds < other.seconds:
            return True
        else:
            return False

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise TypeError("That is not a Clock!")
            return

        if self.hours > other.hours:
            return True
        elif self.hours == other.hours and self.minutes > other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds > other.seconds:
            return True
        else:
            return False

