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
        
