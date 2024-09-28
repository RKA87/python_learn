'''
task 1
Write a Python program to create a person class. 
Include attributes  like name, country and date of birth. Implement a method to  determine the person’s age.
'''
class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob

    def calculate_age(self,dob):
        import datetime
        current_date=datetime.datetime.now()
        current_year=current_date.year
        input_dob=datetime.datetime(dob[0],dob[1],dob[2])
        input_year=(input_dob.year)
        person_age=(current_year-input_year)
        return person_age

t=(1987,9,25)
x=Person("rakesh","india",t)
age=x.calculate_age(t)

print("Name of the Person:",x.name)
print("Name of the Country:",x.country)
print("Date of Birth:",x.dob)
print("Current Age=:",age)

'''
task 2:
Write a Python program to create a class representing a bank. 
Include methods for managing customer accounts and transactions.
'''
class Bank:
    
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
      
    def account_number(self):
        import random
        account_number=random.randrange(111111111,222222222)
        customer_data={self.name:account_number}
        return customer_data

    def account_create(self):
        initial_deposit=0
        data=self.account_number()
        keys=data.keys()
        if self.name in keys:
            print("Key with customer name found so account already exist")
        else:
            self.account_number()
            print("Account Create with Initial Balance is 0")
            
    def make_deposit(self):
        pass      

    def withdrawl(self):
        pass
        
    def display_balance(self):
        pass

dob=(1990,6,27)
x=Bank("Rakesh",dob)
info=x.account_number()
print(info)

dob1=(1991,7,25)
y=Bank("Sujana",dob1)
info1=y.account_number()
print(info1)
y.account_create()

'''
3. Write a Python program to create a class representing a shopping cart. 
Include methods for adding and removing items, and calculating the total price. 
'''
class ShoppingCart:
    def __init__(self):
        self.cart_items=[]

    def add_itmes(self,items):
        self.cart_items.extend(items)
        print("Shopping Cart Added Elements List:",self.cart_items)
    
    def remove_items(self,items):
        for item in items:
            if item in self.cart_items:
                self.cart_items.remove(item)
        print("After Elements Removed Final Cart Items:",self.cart_items)

cart_list=["itme1","item2","item3","item4","item5","item6","item7"]

s=ShoppingCart()
s.add_itmes(cart_list)

remove_list=["itme1","item3","item5","item7"]
s.remove_items(remove_list)

'''
4. Write a Python program to create a calculator class. 
Include methods for basic arithmetic operations
'''
class Calculator:
    
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    
    def add(self):
        print("Addition Result:",(self.n1+self.n2))
    
    def multiplication(self):
        print("Multiplication Result:",(self.n1*self.n2))

    def subraction(self):
        print("Subraction Result:",(self.n1-self.n2))

x=2
y=3
Result=Calculator(x,y)
Result.add()
Result.subraction()
Result.multiplication()

'''
task 5

Write a Python program to create a class that represents a shape. 
Include methods to calculate its area and perimeter.
Implement subclasses for different shapes like circle, triangle, and square.
'''
# Define a base class called Shape
class Shape:

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

# Define a derived class called Circle
class Circle(Shape):
    def __init__(self,r):
        self.r=r
  
    def calculate_area(self): #Method Override from Shape base class
        import math
        return math.pi * self.r**2

    def calculate_perimeter(self): #Method Override from Shape base class
        import math
        return 2 * math.pi * self.r

# Define a derived class called Square
class Square(Shape):
    def __init__(self,side_length):
        self.side_length=side_length
    
    def calculate_area(self):
        return self.side_length*self.side_length
    
    def calculate_perimeter(self):
        return 4*self.side_length

# Define a derived class called Rectangle
class Rectangle(Shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2*(self.length + self.width)

# Define a derived class called Triangle
class Triangle(Shape):

    def __init__(self,base,height,side1,side2,side3):
        self.base=base
        self.height=height
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def calculate_area(self):
        return 0.5 * self.base * self.height
    def calculate_perimeter(self):
        return self.side1+self.side2+self.side3


#For calling Circle   
r=7
circle=Circle(r)
x=circle.calculate_area()
print(x)

#For calling Square
s=5
square=Square(5)
res1=square.calculate_area()
print(res1)
res2=square.calculate_perimeter()
print(res2)

#For calling Rectangle
l=7
w=5
rectangle=Rectangle(l,w)
res3=rectangle.calculate_area()
print(res3)
res4=rectangle.calculate_perimeter()
print(res4)

#For calling Triangle
base=5
height=7
side1=4
side2=6
side3=8
triangle=Triangle(base,height,side1,side2,side3)
res5=triangle.calculate_area()
print(res5)
res6=triangle.calculate_perimeter()
print(res6)

