'''
Write a class Person that takes 3 attributes 
- age, id and name and make them accessible only through getters.
'''
class Person:
    def __init__(self,id,name):
        self.__id=id
        self.__name=name

    # def get_attributes(self):
    #     print("Getting Attributes Details")
    #     return self._age, self._id, self._name
    
    def get_age(self):
        return self.__age
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def set_age(self,x):
        self.__age=x
    
    # def set_id(self,y):
    #     self.__id=y

    # def set_name(self,z):
    #     self.__name=z

    # def set_attributes(self,x,y,z):
    #     print("Setting Attributes")
    #     self._age=x
    #     self._id=y
    #     self._name=z
    #     print("Age:",x)
    #     print("ID:",y)
    #     print("Name:",z)
    
obj=Person(22,1101,'Rakesh')
result=obj.get_age()
print("Age:",result)

class Person1:
    def __init__(self):
        self.__age = None
        self.__id = None
        self.__name = None
        self.__salary=10000
    
    def get_age(self):
        return self.__age
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    def set_age(self,x):
        self.__age=x
    
    def set_id(self,y):
        self.__id=y

    def set_name(self,z):
        self.__name=z

    def set_salary(self,s):
        self.__salary=s

    # def get_attribute_info(self):
    #     return self._age,self._id,self._name

    # def get_attributes(self):
    #     print("Getting Attributes Details")
    #     return self.get_attribute_info()

x=Person1()
age=x.set_age(22)
print(x.get_age)
'''
Another type example
'''
class Person2:

    def __init__(self,age,id,name):
        self.age=age
        self.id=id
        self.name=name

# converting the attributes into private using @property
    @property
    def age(self):
        return self.__age
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @age.setter
    def age(self,age):
        self.__age=age

    @id.setter
    def id(self,id):
        self.__id=id
    
    @name.setter
    def name(self,name):
        self.__name=name
user=Person2(22,1001,"Rakesh")
print(user.name)
user.name="Ramesh"
print(user.name)

'''
Need to chek with Sir

Here syntax is isinstance(obj,type) ->obj is mandatory, type you can pass anything class or datatype

Write a class User that has 2 attributes - id (integer) and name (string) 
[Hint: use typing for defining the attribute types}. 
Override the equals magic method to define 2 user instances to be equal when their ids are equal.  
Show this through an example.
'''
class User:
    def __init__(self,id:int,name:str):
        self.id=id
        self.name=name
    
    def __eq__(self, value: object) -> bool:
        pass

    def __eq__(self, value: object) -> bool:
        if isinstance():
            self.id == value
        pass
      
a=User()
a.id=27
a.name="John"

b=User()
b.id=27
b.name="Deer"

'''
having question on setters, if we are expecting input from outside and pass here

Write a class Student, which defines the attributes - id, marks of 6 subjects in an array 
(use typing for marks to contain only integers). Using setters ensure that the marks are non negative. 
Write methods to return the average, total and highest marks (individual methods)
'''
class Student:   
    marks_list=[]

    while len(marks_list)<6:
        mark=int(input("Enter Subject Marks:"))
        marks_list.append(mark)
        
    def __init__(self,id:int):
        self.id=id
       
    def f_marks_list(self):
        _final_mark_list=[]
        for element in Student.marks_list:
            x=str(element)
            if x[0].startswith("-"):
                x=x[1:]
                x=int(x)
            else:
                x=int(x)
            _final_mark_list.append(x)
        return _final_mark_list
         
    def marks_sum(self):
        return sum(self.f_marks_list())
    
    def avg(self):
        avg=self.marks_sum()/len(self.f_marks_list())
        return avg
    
    def high_mark(self):
        highest_mark=max(self.f_marks_list())
        return highest_mark
    
obj1=Student(22)
print("Student ID:",obj1.id)
obj1.marks_list
m_list=obj1.f_marks_list()
print("Final Mark List:",m_list)
total_marks=obj1.marks_sum()
print("Total Sum of Marks:",total_marks)
average=obj1.avg()
print("Average Marks:",average)
highest_mark=obj1.high_mark()
print("Highest Marks:",highest_mark)

# Need to check with sir
class Student1:
    def __init__(self,id:int):
        self.id=id
        self._marks_list=[]

    #First Get Property
    # @markslist    
    def marks_list(self):
        return self._marks_list
    
    #Set the Markslist of Non-Negative element
    # @markslist.setter
    def set_marks(self):
        final_mark_list=[]
        l=self.marks_list()
        for element in l:
            x=str(element)
            if x[0].startswith("-"):
                x=x[1:]
                x=int(x)
            else:
                x=int(x)
            final_mark_list.append(x)
        return final_mark_list
'''
Need to check with sir, on Class to be define 

A Bank offers different interest rates on the principal amount to different account types 
(savings, current, fixed). 
They intend to add a new account type in the future - NRI - fixed,
the rate of calculation of interest of this type is NOT known yet and will be decided in the future. 
The bank however offers 6.5% interest annually on savings accounts and 9% annually on fixed deposits 
for the fixed deposits with 3 years tenure. 
Please develop a Bank class and account class and define an interest method that returns the interest. 
Also provide ability to define interest for the new account type.
'''
class Bank:
    pass

class Account:
    def __init__(self,name:str,age:int,dob:str,pan_id:str):
        self.name=name
        self.age=age
        self.dob=dob
        self.pan_id=pan_id
        
        self.savings_balance = 0
        self.current_balance = 0
        self.fixed_deposit_balance = 0
        self.nri_balance = 0
    
    def savings_acc(self,money_deposit:int,initial_balance=0):
        self.savings_balance=initial_balance+money_deposit
        print("Savings Account Created")
        return self.savings_balance
    
    def current_acc(self,money_deposit:int,initial_balance=0):
        self.current_balance=initial_balance+money_deposit
        print("Current Account Created")
        return self.current_balance

    def fixed_deposit_acc(self,money_deposit:int,initial_balance=0):
        self.fixed_deposit_balance=initial_balance+money_deposit
        print("Fixed Deposit Account Created")
        return self.fixed_deposit_balance

    def nri_acc(self,money_deposit:int,initial_balance=0):
        self.nri_balance=initial_balance+money_deposit
        print("NRI Account Created")
        return self.nri_balance

    def saving_acc_interest_calc(self):
        p=self.savings_balance
        time=3 #time is 3 years
        rate=6.5
        si=(p*time*rate)/100
        return si
    
    def fixed_dep_interest_calc(self):
        p=self.fixed_deposit_balance
        time=3 #time is 3 years
        rate=9
        fi=(p*time*rate)/100
        return fi
    
    def nri_acc_interest_calc(self,rate):
        p=self.nri_balance
        time=3
        nri_interest=(p*time*rate)/100
        return nri_interest

'''
A company wishes to print the Addresses of its customers in the following format. 
The address is a class with the attributes - address1, address2, city, state, zip. 
Define the from and to addresses and print it in the format given below 
(imagine all the addresses as in a list and the addresses are printed in a page and they cut the slip and paste it).
Hint: use the magic method __repr__ to format the addresses.
'''
class Address:
    def __init__(self,address1:str,address2:str,city:str,state:str,zip:int):
        self.address1=address1
        self.address2=address2
        self.city=city
        self.state=state
        self.zip=zip
         
    def __repr__(self):
        return f'''From:                               To: 
Address1: {self.address1:<25} Address1: {self.address1:<25}
Address2: {self.address2:<25} Address2: {self.address2:<25}
City:     {self.city:<25} City:     {self.city:<25}
State:    {self.state:<25} State:    {self.state:<25}
ZipCode:  {self.zip:<25} ZipCode:  {self.zip:<25}
'''
obj=Address("6911 State Hwy 161","APT:138","IRVING","TX","75039")
info_to_print=obj.__repr__()
print(info_to_print)

'''
Write a Point class in python which takes the x and y coordinates. 
The distance between 2 points is given by the formula. You are given 2 points.
Write a method distance that calculates the distance between 2 points. 
Using this formula calculate the distance between 2 points  shown in the diagram
'''
class Point:
    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

    def distance(self):
        import math
        d=((self.x2-self.x1)*(self.x2-self.x1))+((self.y2-self.y1)*(self.y2-self.y1))
        d=math.sqrt(d)
        return d
        
obj=Point(7,5,4,1)
res=obj.distance()
print("Resultant SquareRoot Value:",res)

'''
Need to check with sir on calling the Point Class

Using the point class above, define a class Triangle that takes 3 coordinates and calculates the area. 
The base class The area of the equilateral triangle is given below.  
Write a method to returns the area. Also write another method that says if the triangle is equilateral or not. 
Only if the triangle is an equilateral triangle the area should be calculated using the below formula. 
Else it should display an error. Show this through an example
'''
# class Triangle(Point):
#     def __init__(self,x1,x2,y1,y2):
#         super().__init__(x1,x2,y1,y2)

class Triangle:
    def __init__(self,side1,side2,base):
        self.s1=side1
        self.s2=side2
        self.base=base
 
    def __triangle_area(self):
        import math
        area=(math.sqrt(3)/4)
        area=area*(self.s1*self.s2)
        return area
    
    def triangle_eq_or_not(self):
        if self.s1==self.s2==self.base:
            return self.__triangle_area()
        else:
            print("The side & base coordinates are not equal so it is not equilateral triangle")
            return None

obj3=Triangle(5,7,7)
result=obj3.triangle_eq_or_not()
print("Result of Area:",result)

'''
Need to check with sir, regarding 4 coordinates

You have a class Shape which defines 4 coordinates. It also defines methods area and perimeter, 
The class is an abstract class as both the methods area and perimeter cannot be calculated as the shape could be 
a rectangle or a square. 
It defines a method distance that returns the distance between 2 coordinates. 
Define 2 classes Rectangle and Square which derives the Shape class and returns the area and perimeters. 
'''
class Shape():
    def __init__(self,a:int,b:int,c:int,d:int):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def calculate_area(self): #Method Overriding
        return self.side**2
    
    def calculate_perimeter(self): #Method Overriding
        return 4*self.side

class Rectangle(Shape):
    def __init__(self,length:int,width:int):
        self.length=length
        self.width=width

    def calculate_area(self): #Method Overriding
        return self.length * self.width
    
    def calculate_perimeter(self): #Method Overriding
        return 2*(self.length + self.width)

'''
Want to check with sir, regarding the 12 squares

There is a class Square. It has an attribute side and its area is given by side x side. 
What is the area of the following image. 
You need to define 12 squares each with their ids and then calculate the total area
''' 

'''
In the above example, how can you determine if a given triangle is a right angle triangle?
'''

class IsoscelesTriangle(Triangle):
