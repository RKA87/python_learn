# StaticMethod to define in Python using Properties which is called @staticmethod
# StaticMethod will never use Self in the code, its called Class Methods
# Will define Self only instance methods

class Animal:
    _animalvariable="This Animal is called"

    def about(self):
        print("Info:"+ self._animalvariable + "!")


class Dog(Animal):
    _animalvariable="This Animal is called Dog"

class Tiger(Animal):
    _animalvariable="This Animal is called Tiger"

instance1=Animal()
instance1.about()

instance2=Dog()
instance2.about()

instance3=Tiger()
instance3.about()

# Defining StaticMethod in class. 
# The @staticmethod decorator makes it clear that these methods don’t use self or cls

class Animal:
    _animalvariable="This Animal is called"

    @staticmethod
    def about():
        print("Info:"+ Animal._animalvariable + "!")
    
class Cheeta(Animal):
    _animalvariable="This Animal is called Cheeta"

class Lionness(Animal):
    _animalvariable="This Animal is called Lionness"

Animal.about()
Cheeta.about()
Lionness.about()

#Using Static Method examples

class Temperature:
    statement="After Conversion, Weather Records as:"

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsisu(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def about():
        print("Info:" + Temperature.statement)
    

class Test1(Temperature):
    Temperature.statement="Conversion Weather"

class Test2(Temperature):
    pass

Test1.about()
print(Test1.celsius_to_fahrenheit(40))
