import random

class Robot:

    __illegal_names={"Henry","Oscar"}
    __crucial_health=0.6

    def __init__(self,name):
        self.name=name
        self.health_level=random.random()
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        if name in Robot.__illegal_names:
            self.__name="Marvin"
        else:
            self.__name=name
    
    #String Method to define the exact info want to print when the instance executed
    def __str__(self) -> str:
        return self.name + " Robot" #name is coming from the getter property
    
    def __add__(self,other): #by default addition has two so second one is here nothing but other
        first=self.name.split("-")[0]
        second=other.name.split("-")[0]
        return Robot(first + "-" + second)
    
    def needs_a_nurse(self):
        if self.health_level < Robot.__crucial_health:
            return True
        else:
            return False
    
    def say_hi(self):
        print("Hi, I am", self.name)
        print("My health level is: ", self.health_level)

first_generation = (Robot("Marvin"), Robot("Engima-Alan"), Robot("Charles-Henry")) #you can assign the instance as a tuple for the class

print(first_generation) # Here we get the Memory reference value

# we can get ouptut as we expect __str__() format
# first_generation= " ,".join(str(robot) for robot in first_generation)
# print("String formatted output:",'\n',first_generation)

gen1=first_generation


# babies=[gen1[0] + gen1[1], gen1[1] + gen1[2]]
# print(babies)
# babies.append(babies[0]+babies[1])
# print(babies)

# for baby in babies:
#     baby.say_hi()


