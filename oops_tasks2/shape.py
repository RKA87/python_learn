from abc import ABC, abstractmethod
from point import Point

class Shape(ABC):
    def __init__(self,a:Point,b:Point,c:Point,d:Point):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

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

    
    @property
    def d(self):
        return self.__d
    
    @d.setter
    def d(self,d:Point):
        self.__d=d
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,a:Point,b:Point,c:Point,d:Point,e,f):
        super().__init__(a,b,c,d,e,f)
        self.e=e
        self.f=f

    def distance(self):
        self.
        self.a
        d1=self.a.distance(self.b)
        d2=self.b.distance(self.c)
        d3=self.c.distance(self.d)
        d4=self.d.distance(self.a)
        return d1, d2, d3, d4
    
    def area(self):
        d1,d2,d3,d4=self.distance()
        width=d1*d2
        height=d3*d4
        area_value=width*height
        return width, height, area_value
    
    def perimeter(self):
        width,height,area_value = self.area()
        return 2*(width+height)

a = Point(1, 2)
b = Point(3, 2)
c = Point(3, 4)
d = Point(1, 4)

obj=Rectangle(a,b,c,d)
print("Area of Rectangle:", obj.area()[2])
print("Perimeter of Rectangle:",obj.perimeter())

class Square(Shape):
    def __init__(self,a:Point,b:Point,c:Point,d:Point):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self,a):
        self.__a=a

    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self,b):
        self.__b=b

    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self,c):
        self.__c=c

    @property
    def d(self):
        return self.__d
    @d.setter
    def d(self,d):
        self.__d=d
    
    def distance(self):
        
    
    def area(self):
        area_of_square=