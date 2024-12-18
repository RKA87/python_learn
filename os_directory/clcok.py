class Clock:
    def __init__(self, hours, minutes, seconds):
        self.set_clock(hours, minutes, seconds)

    def set_clock(self, hours, minutes, seconds):

        if type(hours)==int and hours >=0 and hours <24:
            self._hours=hours
        else:
            raise TypeError("Hours have to be integers between 0 to 23!")
        
        if type(minutes)==int and minutes >=0 and minutes <60:
            self._minutes=minutes
        else:
            raise TypeError("Minutes have to be integers between 0 to 59!")
        
        if type(seconds)==int and seconds >=0 and seconds <60:
            self._seconds=seconds
        else:
            raise TypeError("Seconds have to be integers between 0 to 59!")
    
    def __str__(self) -> str:
        return "{0:02d}:{1:02d}:{2:02d}".format(self._hours, self._minutes, self._seconds)

    def tick(self):
        if self._seconds == 59:
            self._seconds=0
            if self._minutes == 59:
                self._minutes=0
                if self._hours == 23:
                    self._hours=0
                else:
                    self._hours +=1
            else:
                self._minutes +=1
        else:
            self._seconds +=1

x=Clock(23,59,59)
print(x)
for second in range(0,6):
    try:        
        x.tick()
        print(x)
        print(x)
    except Exception as E:
        print("Error Exception:", E)        