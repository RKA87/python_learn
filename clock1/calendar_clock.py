from calendar import Calendar
from clock  import Clock

class CalendarClock(Clock, Calendar):
    def __init__(self,d:int,m:int,y:int,hours:int,minutes:int,seconds:int):
        # super().__init__() #question, why not define here like this?
        Clock.__init__(self,hours, minutes, seconds)
        Calendar.__init__(self,d,m,y)
    
    def tick(self):
        """
        advance the clock by one second
        """
        previous_hour = self._hours
        Clock.tick(self) #in heritance class Clock method called here
        if (self._hours < previous_hour): 
            self.advance() # in heritance class Calendar method called here

    def __str__(self):
        return Calendar.__str__(self) + "," + Clock.__str__(self)

        
x = CalendarClock(31, 12, 2013, 23, 59, 59)
print("One tick from ",x, end=' ')
x.tick()
print("to",x)
