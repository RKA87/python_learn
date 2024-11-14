# Multiple InHeritance
from typing_extensions import Type

class Clock:
    def __init__(self,hours:int, minutes:int, seconds:int):
        self.set_Clock(hours, minutes, seconds)

    def set_Clock(self,hours, minutes, seconds):
        if type(hours) == int and hours >= 0 and hours < 24:
            self.__hours=hours
        else:
            