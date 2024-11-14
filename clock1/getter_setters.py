# #1st Method
# class Test1:
#     def __init__(self,x:int,y:str):
#         self.__x=x
#         self.__y=y

#     @property
#     def x(self):
#         return self.__x
    
#     @x.setter
#     def x(self,x):
#         self.__x=x

#     @property
#     def y(self):
#         return self.__y
    
#     @y.setter
#     def y(self,y):
#         self.__y=y
    
# inst1=Test1(27,"Rakesh")
# print("Number:", inst1.x)
# print("Name:",inst1.y)

#2nd Method
class Person:
    def __init__(self,name:str,height:int):
        self.__name=name
        self.height=height

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name=name
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,value):
        if value < 6:
            raise Exception("Height should be Greater than 6")
        else:
            self.__height=value

inst1=Person("Rakesh",7)
print("Name:", inst1.name)

print("Height:", inst1.height)