'''
Attributes can be defined at any time in python

you can define attribute to an object or an class directly like below
'''
class Robot:
    pass

#Assigning an attribute to the class.
Robot.name="Ram"

def func(x):
    print("Hi,This is", x.call) #assigning an attribute to the object 'x'

#assigning an attribute to the fucntion
func.call="Raju"

obj=Robot()
obj.call="value"

func(obj)


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
        self.age=age #it will call line 132
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
        if isinstance(value,User):
            return self.id == value.id and self.name == value.name
        else:
            return False

x1=User(22,"Rakesh")
x2=User(22,"Ram")
x1.id=22
x2.id=23
print(x1.id==x2.id)

'''
having question on setters, if we are expecting input from outside and pass here

Write a class Student, which defines the attributes - id, marks of 6 subjects in an array 
(use typing for marks to contain only integers). Using setters ensure that the marks are non negative. 
Write methods to return the average, total and highest marks (individual methods)
'''
import typing
from typing import List

class Student:   
    marks_list=[] # it can be shared among all instances in a class, which means its a class variable. Not good.

    while len(marks_list)<6:
        mark=int(input("Enter Subject Marks:"))
        marks_list.append(mark)
        
    def __init__(self,id:int, marks_list:List(int)): # type: ignore
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

    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self,x):
        self.__x=x

    @y.setter
    def y(self,y):
        self.__y=y
    
    def distance(self,point):
        if isinstance(point,Point):
            import math
            distance=math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
            return distance
        
A=Point(1,2)
B=Point(1,5)
output=(B.distance(A)) 
print("Distance:", output)

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

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def distance(self,point):
        import math
        if isinstance(point,Point):
            distance=math.sqrt((self.x-point.x)**2+(self.y-point.y)**2)
            return distance

a=Point(1,2)
b=Point(1,5)
print("Distance:",b.distance(a))

''''
Instead of In-Heritance Concept, here we've used Composition concept.
Most important things to observe and learn
'''
class Triangle:
    def __init__(self,p1,p2,p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3
    
    def _distance_length(self):
        s1=self.p1.distance(self.p2)
        s2=self.p1.distance(self.p3)
        s3=self.p2.distance(self.p3)
        return s1, s2, s3
    
    def area_of_equilateral_triangle(self):
        import math
        value=(math.sqrt(3)/4)
        s1,s2,s3 = self._distance_length()
        area=value*(s1**2)
        return area
    
    def check_equilateral_triangle(self):
        s1,s2,s3=self._distance_length()
        if s1==s2==s3:
            return self.area_of_triangle()
        else:
            print("Given Points not form an Equilateral Triangle")
            return None

'''
You have a class Shape which defines 4 coordinates. It also defines methods area and perimeter, 
The class is an abstract class as both the methods area and perimeter cannot be calculated as the shape could be a rectangle or a square. 
It defines a method distance that returns the distance between 2 coordinates. 
Define 2 classes Rectangle and Square which derives the Shape class and returns the area and perimeters.
'''

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def distance(self,point):
        import math
        if isinstance(point,Point):
            distance=math.sqrt((self.x-point.x)**2+(self.y-point.y)**2)
        return distance
        
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self,p1,p2,p3,p4):
        super().__init__(p1,p2,p3,p4)
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self,p1,p2,p3,p4):
        super().__init__(p1,p2,p3,p4)

    
    def area(self):
        length=self.p1.distance(self.p2)
        width=self.p2.distance(self.p3)
        area=length*width
        return area
    
    def perimeter(self):
        width=self.p2.distance(self.p3)
        length=self.p3.distance(self.p4)
        perimeter=2*(length+width)
        return perimeter
    

class Square(Shape):
    def __init__(self,p1,p2,p3,p4):
        super().__init__(p1,p2,p3,p4)
    
    def area(self):
        value=self.p1.distance(self.p2)
        area=value*value
        return area
    
    def perimeter(self):
        value=self.p3.distance(self.p4)
        perimeter=4*value
        return perimeter

'''
Want to check with sir, regarding the 12 squares

There is a class Square. It has an attribute side and its area is given by side x side. 
What is the area of the following image. 
You need to define 12 squares each with their ids and then calculate the total area
''' 

'''
In the above example, how can you determine if a given triangle is a right angle triangle?
'''
class RightAngleTriangle:
    def __init__(self,side_angle1,side_angle2,side_angle3):
        self.side_angle1=side_angle1
        self.side_angle2=side_angle2
        self.side_angle3=side_angle3

    def right_angle_triangle(self):
        if (self.side_angle1==90) or (self.side_angle2 == 90) or (self.side_angle3 == 90):
            return True
        else:
            res=("Given Input anyone of the side angle is not in 90degree")
            return res
angle=RightAngleTriangle(75,27,84)
print(angle.right_angle_triangle())

'''
I have a Point represented by its x and y coord (1,2) and 
I have a rectangle defined by the coordinates (shown in the diagram below).

Write a method is_point_in_rectangle() which takes a point and tells if the point lies within the rectangle or not.
Reuse the Point class defined above. 
'''
# x=6
# y=5

# for i in range (0,7):
#     for j in range(0,6):
#         print(i,j,end=" ")
#         print('\n')

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def is_point_in_rectangle(self):
        if self.x in range (0,7) and self.y in range(0,6):
            print("Co-Ordinates are with in Rectangle Range")
        else:
            print("Co-Ordinates are not in range")

result=Point(8,5)
result.is_point_in_rectangle()

'''
Points Inside, Outside or On a circle - follow the link at
https://www.khanacademy.org/math/geometry/hs-geo-analytic-geometry/hs-geo-dist-problems/v/point-re
lative-to-circle#:~:text=First%2C%20find%20the%20equation%20for,is%20inside%20of%20the%20circle 
and implement the logic to tell if a point lies within, outside or on the circle. 
'''

class InOutOnCircle:
    def __init__(self,*args:tuple):
        self.args=args

    def tuple_int(self):
        if len(self.args)!=1 or not isinstance(self.args[0],tuple) or len(self.args[0]!=2):
            raise ValueError ("Please provide a single with exactly two elements")
    
    def point_lies(self):
        (x,y)=self.args[0]
        import math
        distance=(x**2+y**2)
        result=math.sqrt(distance)
        if result > 6:
            print("Outside of Circle")
        if result == 6:
            print("On the Cirlce")
        if result < 6:
            print("Inside the Circle")

'''
The company taxes its customers at a flat rate of 10% on the goods value. 
The distributors add 7% on the goods value in addition to the companys tax.  
The wholesalers add 5% on the goods value and the retailers add 2% on the goods value. 
Calculate the final amount payable by the customer on a product say Book whose cost is Rs. 100. 
Implement a design using OOPS to enable code reuse and extensibility.
'''
class GoodsCost:
    def __init__(self,*args):
        self.args=args
    
    def __products(self):
        product_list=[]
        product_list=[product for product in self.args]
        return product_list
    
    def caclculate_taxes(self):
        flat_rate_margin=(100*0.10) #10%
        distributor_margin=(100*0.07) #7%
        wholesale_margin=(100*0.05) #5%
        retailers_margin=(100*0.02) #2%
        taxes_amount=flat_rate_margin+distributor_margin+wholesale_margin+retailers_margin
        return taxes_amount
    
    def final_amount(self):
        product_prices=self.__products()
        base_price=100
        amount=len(product_prices)*base_price
        final_price=amount+self.caclculate_taxes()
        return final_price


obj=GoodsCost("book1", "book2", "book3")
result=obj.final_amount() 
print("Final Price:",float(result))


'''
A Person earns Rs. 10K per month.  
He gets Rs. 20K from her Father’s property as rent and Rs. 15K as rent from his mother’s property. 
He also gets a monthly fixed pension of his grandfather of Rs. 30K. 
What is the person’s annual income? Design a solution using OOPS.
'''

class PersonAnnualIncome:

    def __init__(self,person_income,fp_income,mp_income,gf_income):
        self.__person_income=person_income
        self.__fp_income=fp_income
        self.__mp_income=mp_income
        self.__gf_income=gf_income

    @property
    def person_income(self):
        return self.__person_income
    
    @property
    def fp_income(self):
        return self.__fp_income
    
    @property
    def mp_income(self):
        return self.__mp_income
    
    @property
    def gf_income(self):
        return self.__gf_income
    
    #setter the value    
    @person_income.setter
    def person_income(self,pi):
        self.__person_income=pi

    @fp_income.setter
    def fp_income(self,fp):
        self.__fp_income=fp
    
    @mp_income.setter
    def mp_income(self,mp):
        self.__mp_income=mp


    @gf_income.setter
    def gf_income(self,gf):
        self.__gf_income=gf
    
    def annual_income(self):
        annual_income=12*(self.__person_income+self.__fp_income+self.__mp_income+self.__gf_income)
        return annual_income
'''
Design a class Paragraph, which has words. The words comprise many letters. 
Write a method that returns the total words and total letters in a Paragraph. (2 different methods)
'''
class Paragraph:
    
    def __init__(self,file_path:str):
        self.file_path=file_path
        
    def get_raw_data(self):
        try:
            with open(self.file_path, 'r') as data:
                raw_data=data.read()
        except FileNotFoundError as E:
            print(E)
        return raw_data

    def words_total(self,raw_data): 
        words_output=raw_data.split(" ")
        return (len(words_output))

    def words_length(self,raw_data):    
        length=0
        words=raw_data.split(" ")
        for word in words:
            length += (len(word))
        return length
    
file_path="C:/Temp/test_file.txt"
obj=Paragraph(file_path)
res=obj.get_raw_data()
print("Raw Data:",res)

res1=obj.words_total(res)
print("Total Words:",res1)

res2=obj.words_length(res)
print("Total Length of Words:",res2)