class Calendar:
    months=(31,28,31,30,31,30,31,31,30,31,30,31)
    date_style="British"

    @staticmethod
    def leapyear(year):
        if not year %4 == 0:
            return False
        elif not year %100 == 0:
            return True
        elif not year %400 == 0:
            return False
    
    def __init__(self,d,m,y):
        self.set_Calendar(d,m,y)
    
    def set_Calendar(self,d,m,y):
        if type(d) == int and type(m) == int and type(y) == int:
            self.__days=d
            self.__months=m
            self.__years=y
        else:
            raise TypeError ("d, m, y have to be Integers!")
    
    def __str__(self):
        if Calendar.date_style == "British":
            return "{0:02d}/{1:02d}/{2:02d}".format(self.__days, self.__months, self.__years)
        else:
            return "{0:02d}/{1:02d}/{2:02d}".format(self.__months, self.__days, self.__years)

x = Calendar(31,12,2012)
y = Calendar(30,7,2024)

print(y.date_style)
print(x.date_style)
print(Calendar.date_style)
print(Calendar.months)
print(Calendar.months[11])
print(x, end=" ")
x.date_style="India"
print(y.date_style)

print(Calendar.leapyear(2020))


    
