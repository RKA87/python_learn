class Calendar:
    months=(31,28,31,30,31,30,31,31,30,31,30,31)
<<<<<<< HEAD
    date_style = "British"

    @staticmethod
    def leapyear(year):
        if not year % 4 == 0:
            return False
        elif not year % 100 == 0:
            return True
        elif not year % 400 == 0:
            return False
        else:
            return True
    
    def __init__(self, d, m, y):
        self.set_Calendar(d,m,y)
    
    def set_Calendar(self, d, m, y):
        if type(d) == int and type(m) == int and type(y) == int:
            self.__days = d
            self.__month = m
            self.__year = y
        else:
            raise TypeError("d, m, y have to be integers!")
    
    def __str__(self):
        if Calendar.date_style == "British":
            return "{0:02d}/{1:02d}/{2:04d}".format(self.__days, self.__month, self.__year)
        else:
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__month, self.__days, self.__year)
    
    def advance(self):
        max_days = Calendar.months[self.__month-1]
        if self.__month == 2 and Calendar.leapyear(self.__year):
            max_days +=1
        if self.__days == max_days:
            self.__days = 1
            if self.__month ==12:
                self.__month =1
                self.__year +=1
            else:
                self.__month +=1
        else:
            self.__days += 1
            
x = Calendar(31,12,2012)
print(x) #, end=" ")




=======
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
    
    def advance(self):
        """
        This method advances to the next date.
        """

        max_days = Calendar.months[self.__months-1]
        if self.__months == 2 and Calendar.leapyear(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days= 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1


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


    
>>>>>>> 23563f29be6fa11ba1def91061921847b50f4daf
