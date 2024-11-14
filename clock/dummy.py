class Dummy:
    def __init__(self,x):
        self.x=x
    
    def __str__(self) -> str:
        # print(self.x)
        return self.x

inst=Dummy("parameter1")
print(inst)

print(Dummy("ram"))

