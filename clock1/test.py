from typing import Any


class Person:
    def __init__(self,name,height):
        self.name=name
        self.height=height

    def __str__(self):
        return self.name
    
    def __repr__(self) -> str:
        return f"My Name is: {self.name} and I'm {self.height}cms"

    def __len__(self):
        if self.height > 165:
            return self.height
        else:
            return 165
            
        

x=Person("Rakesh", 170.18)
print((x))
print(type((x)))

try:
    with open('text.txt', encoding="utf-8") as f:
        for line in f:
            print(line.strip())
except Exception as E:
    print("Error:", E)

# def print_pattern(n:int):
#     char="*"
#     for row in range(n):
#         for col in range(row+1):
#             print(char, end=" ")
#         print(" ")

# n=int(input("Enter a Number:"))
# print_pattern(n)


    