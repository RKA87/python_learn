class Point:
    def __init__(self,x:int,y:int):
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
    
    def distance(self,point):
        import math
        if isinstance(point,Point):
            distance=math.sqrt((point.y-self.y)**2+(point.x-self.x)**2)
            return distance

obj1=Point(3,7)
obj2=Point(2,8)

d=obj1.distance(obj2)
print("Distance b/w two points:",d)