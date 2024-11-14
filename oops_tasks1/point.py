class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,x):
        self.__x=x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,y):
        self.__y=y
    
    def distance(self,other):
        import math
        if isinstance(other,Point):
            distance=math.sqrt((other.y-self.y)**2+(other.x-self.x)**2)
            return distance

A=Point(1,3)
B=Point(2,5)
d=B.distance(A)
print("Distance:",d)