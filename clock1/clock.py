# Multiple InHeritance
from typing_extensions import Type

class Clock:
    def __init__(self,hours:int, minutes:int, seconds:int):
        self.set_Clock(hours, minutes, seconds)

    def set_Clock(self,hours, minutes, seconds):
        if type(hours) == int and hours >= 0 and hours < 24:
            self._hours=hours
        else:
            self._hours=hours
        if type(minutes) == int and minutes >=0 and minutes <60:
            self.__minutes=minutes
        else:
            self.__minutes=minutes
        if type(seconds) == int and seconds >=0 and seconds <60:
            self.__seconds=seconds
        else:
            self.__seconds=seconds
    
    def tick(self):
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self._hours == 23:
                    self._hours = 0
                else:
                    self._hours +=1
            else:
                self.__minutes +=1
        else:
            self.__seconds +=1
        
    def __str__(self) -> str:
        return "{0:02d}:{1:02d}:{2:02d}".format(self._hours, self.__minutes,self.__seconds)
   
x=Clock(22,33,59)
print("Before Tick:",x)
x.tick()
print("After Tick:",x)