from clock import Clock
from calendar import Calendar

class CalendarClock(Clock, Calendar):
    
    def __init__(self,d:int,m:int,y:int,hours, minutes, seconds):
        # super().__init__(self,hours, minutes, seconds)
        # super().__init__(self,d,m,y)

        Clock.__init__(self,hours, minutes, seconds)
        Calendar.__init__(self,d,m,y)


    def tick(self):
        """
        advance the clock by one second
        """
        previous_hour = self._hours #self._hours is coming from Clock class which is protected variable
        Clock.tick(self) # here self is coming from Calendar Method
        if (self._hours < previous_hour): 
            self.advance() #you can define it as Calendar.advance()... when it defines self, it means, it will search first in CalendarClock and then it goes to Clock & Calendar
        

    def __str__(self):
        return Calendar.__str__(self) + ", " + Clock.__str__(self)
        
inst=CalendarClock(23,7,2020,23,59,59)
print(inst)
inst.tick()
print(inst)