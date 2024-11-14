from point import Point

class Triangle(Shape):
    def __init__(self,a:Point,b:Point,c:Point):
        self.a=a
        self.b=b
        self.c=c
    
    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self,a:Point):
        self.__a=a
    
    @property
    def b(self):
        return self.__b
    
    @b.setter
    def b(self,b:Point):
        self.__b=b

    @property
    def c(self):
        return self.__c
    
    @c.setter
    def c(self,c:Point):
        self.__c=c
    
    def __side_length(self): #private method using __
        s1=self.a.distance(self.b)
        s2=self.b.distance(self.c)
        s3=self.a.distance(self.c)
        return s1,s2,s3
    
    def area_of_triangle(self):
        s1,s2,s3=self.side_length()
        import math
        area=(math.sqrt(3)/4)*(s1*s1)
        return area
    
    def perimeter_of_triangle(self):
        s1,s2,s3=self.__side_length() #Now private method can be accessible internally in the class only
        return s1+s2+s3

    def check_equilateral(self):
        d1=self.distance(self.a,self.b)
        d2=self.distance(self.b,self.c)
        d3=self.distance(self.c,self.a) #this is not working for me, how it is works for your case?

    def distance(self): # Here I understand in point class, distance method has 1 arg so that i want to method override. in method overide, how would i pass
        #3 arguments?
        #is this is the reason you define this one in abstract class, method?
        #Is this is part of design?

    #so two things to check
    #1. class Triangle(parentclass)
    #2. class Triange: (without parent class) 



a=Point(1,2)
b=Point(3,4)
c=Point(5,6)
obj=Triangle(a,b,c)
print(obj.side_length())
print(obj.check_equilateral())

class Rectangle:
