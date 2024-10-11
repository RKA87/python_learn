class Person2:

    def __init__(self,age,id,name):
        self.age=age
        self.id=id
        self.name=name

# converting the attributes into private using @property
    @property
    def age(self):
        return self.__age
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @age.setter
    def age(self,age):
        self.__age=age

    @id.setter
    def id(self,id):
        self.__id=id
    
    @name.setter
    def name(self,name):
        self.__name=name

