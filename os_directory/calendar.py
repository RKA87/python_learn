class Calendar:

    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    
    def __init__(self,d,m,y):
        self.set_calendar(d,m,y)
    
    def leapyear(year):
        if not year % 4 == 0:
            return False
        elif not year % 100 == 0:
            return True
        elif not year % 400 == 0:
            return False
        else:
            return True
    
    def set_calendar(self,d,m,y):
        if type(d)==int and d >=1 and d <=31:
            self.d=d
        else:
            raise TypeError("Date should 1 to 31!")
        if type(m)==int and m >=1 and m<=12:
            self.m=m
        else:
            raise TypeError("Month should 1 to 12!")
        
        if type(y)==int:
            self.y=y
        else:
            raise TypeError("Date should 1 to 31!")

    def __str__(self) ->str:
        return "{0:02d}/{1:2d}/{2:2d}".format(self.d,self.m,self.y)
    
    def advance(self):
        max_days=Calendar.months[self.m-1] #using input month we will get the max days, if month is 2 you will get 28, if its 1 you will get 31 days
        if self.m==2 and Calendar.leapyear(self.y):
            max_days +=1
        
        if self.d == max_days:
            self.d=1
            if self.m == 12:
                self.m = 1
                self.y += 1
            else:
                self.m +=1
        else:
            self.d += 1

try:
    x=Calendar(15,12,2024)
    print(x)
except Exception as E:
    print("Error:", E)