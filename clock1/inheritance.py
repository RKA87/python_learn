# class Robot:
#     def __init__(self,name):
#         self.name=name

#     def say_hi(self):
#         print("Hi, I am:",self.name)
    
# class PhysicianRobot(Robot):
#     pass

# x=Robot("Marvin")
# y=PhysicianRobot("Ram")

# print(isinstance(x, Robot)) #True
# print(isinstance(y,PhysicianRobot)) #True
# print(isinstance(x, PhysicianRobot)) #False
# print(isinstance(y, Robot)) #True it is subclass of Robot

# print(type(y) == Robot) #type(y) == PhysicianRobot: This checks if y is exactly an instance of PhysicianRobot, which is True

# print(type(y) == PhysicianRobot) # True, this is exactly matches with PhysicianRobot class so equal condition matches to True

# class Robo:
#     def __init__(self,name):
#         self.name=name
    
#     def say_hi(self):
#         print("Hi,I am:", self.name)

# class PhysicianRobo(Robo):
#     def __init__(self, name):
#         super().__init__(name)

#     def say_hi(self):
#         print("Everything will be okay!")
#         print(self.name + " Taking Care of you")

# y=PhysicianRobo("Ram")
# y.say_hi()

'''
Important Notes:

We have seen that an inherited class can inherit and override methods from the superclass. 
Besides this a subclass often needs additional methods with additional functionalities, which do not exist in the superclass

Attribute(helath_level)

    self.health_level = random.random() assigns a random float between 0 and 1 to self.health_level every time a new Robot is created

    Since health_level is set to a random value within the __init__ method, there's no need to pass it as a parameter when creating a Robot. 
    Every instance of Robot will have a unique, randomly generated health_level value without you needing to specify it each time
'''
import random

class Robot:
    def __init__(self,name):
        self.name=name
        self.health_level=random.random()
    
    def say_hi(self):
        print("Hi, I am", self.name)
    
    def needs_a_doctor(self):
        if self.health_level < 0.8:
            return True
        else:
            return False

class PhysicianRobot(Robot):
    def __init__(self, name):
        super().__init__(name)
    
    def say_hi(self):
        print("Everything will be okay")
        print(self.name + "takes care of you")

    def heal(self,parameter):
        parameter.health_level = random.uniform(parameter.health_level,1)
        

        



