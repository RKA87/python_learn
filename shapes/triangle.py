import typing
from point import Point

class Triangle:
    def __init__(self,p1:Point,p2:Point,p3:Point):
        self.p1=p1
        self.p2=p2
        self.p3=p3

    @property
    def p1(self):
        return self.__p1
    
    @property
    def p2(self):
        return self.__p2
    
    @property
    def p3(self):
        return self.__p3
    
    @p1.setter
    def p1(self,p1):
        self.__p1=p1

    @p2.setter
    def p2(self,p2):
        self.__p2=p2

    @p3.setter
    def p3(self,p3):
        self.__p3=p3
    
    # def distance(self):
    #     d1=self.distance(self.p1,self.p2)
    #     return d1

    def length(self):
        m1=p3.distance(p2)

    # def distance(self):
    #     d1=p3.distance(p1)
    #     return d1
    
p1=Point(1,3)
p2=Point(2,4)
p3=Point(4,5)

obj=Triangle(p1,p2,p3)
print(obj.distance())

    

    