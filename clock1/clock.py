# Multiple InHeritance
from typing_extensions import Type

class Clock:
    def __init__(self,hours:int, minutes:int, seconds:int):
        self.set_Clock(hours, minutes, seconds)

    def set_Clock(self, hours, minutes, seconds):
        if type(hours) == int and hours >= 0 and hours < 24:
            self._hours=hours
        else:
            raise Exception ("Hours have to be integers between 0 to 23 only !")
        if type(minutes) == int and minutes >= 0 and minutes <60:
            self.__minutes=minutes
        else:
            raise Exception ("Minutes have to be integers between 0 to 59 only")
        if type(seconds) == int and seconds >= 0 and seconds <60:
            self.__seconds=seconds
        else:
            raise Exception ("Seconds have to be integers between 0 to 59 only")
    
    def __str__(self) -> str:
        # print ("{0:02d}:{1:02d}:{2:02d}".format(self._hours, self.__minutes, self.__seconds))
        return ("{0:02d}:{1:02d}:{2:02d}".format(self._hours, self.__minutes, self.__seconds)) # In Python the __str__ method should return the value but not to print it

    def tick(self):
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self._hours == 23:
                    self._hours = 0
                else:
                    self._hours += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1

try:
    x=Clock(22,43,45)
    print(x)
except Exception as E:
    print("Errro Message:", E)