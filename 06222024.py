'''
Nested Functions Notes

Result store in one function with return ---> call as Result stored function

Main function to be written by specifying to call the "Result Stored Function" with arguments that should match result stored function

Resultant Function is example, by defining/calling the Main function with matched condition of arguments that will be applying to Result stored function

for arguments names should matches exactly like Result Store Function arguments are a & b so the resultant function arguments should be the same

'''

'''
Task 1
Write a function that takes a function and performs the operations like twice, thrice, fource etc.

Ex. increment(fn, 3) 
Should take the respective functions to return twice, thrice etc of the number

'''

def function01(arg1,arg2):
    print("Name:", arg1)
    print("contact No:", arg2)

def function02(arg3):
    # print("Project Name:", arg3)
    return arg3

def function03(arg4):
    print("Role:", arg4)

#case
def test01_fn(**kwargs):
    print(kwargs['x'])
    print(kwargs['y'])

test01_fn(x="RakeshKumar", y="7323229869")


#case
def function01(arg1,arg2):
    print("Name:", arg1)
    print("contact No:", arg2)

def test_fn(fn,**kwargs):
    print("You are calling different function, results will display based on the function that you call")
    return fn(**kwargs)

test_fn(function01, arg1="RakeshKumar", arg2="7323229869")


#case 

def test_args_kwargs(*args, **kwargs):
    l=[]
    for arg in args:
        l.append(arg)
    
    dict = kwargs #Here you can do anything using dictionary methods to get keys, values, key & val as item pairs

    print("Name:",l[0])
    print("Contact:", l[1])
    print("Dictionary:", dict)
          
x=["Rakesh Kumar", "7323229869"]
kwargs = {"E-Mail":"xyz@gmail.com", "E-Mail2":"abc@gmail.com"}
test_args_kwargs( *x,**kwargs )  #If you don't pass * for args, it will be consider as one single element as tuple & dont pass ** for dict it consider as single with empty

# +++++++++++++++++++++++++
'''
Task 2
Re-write the above function to return a function that does the same.
'''
def function04():
    print("Checking function without any arguments")

def rewrite(fn):
    return fn

x = rewrite(function04) #Assigning the function04 in rewrite
x() #now x has return value fn which is function04, to call that which is suppose to be function04()

#case
def test_args_kwargs(name,contact, email):
        
        print(f"Name: {name}") #f string concept it starts with f"<here we have to denote the code>"
        print(f"contact: {contact}")
        print(f"e-mail: {email}")

args = ["RakeshKumar", "7323229869"]
kwargs = {"email": "example@example.com"}

test_args_kwargs(*args, **kwargs) #passing multiple argument values in args using *

'''
Task 3
Write a program to take the function name and parameter as **kwargs and invokes the function with that parameter.  The function and the parameter could be any arbitrary one
'''

import types

#Main Function

def invoke_function(function, **kwargs):
    if isinstance(function, types.FunctionType):
        return function(**kwargs)
    else:
        print("Condition not match")

# Result Stored Function

def add(a,b):
    sum = a+b
    return sum

#Resultant/Executable Function

resultant_function = invoke_function(add, a=7, b=7) #now resultant_function output has add(**kwargs) this means add(a=7,b=7) a,b arguments work like as assigned values will be applied to add(a,b) wh
print(resultant_function)

'''
Task 4
Write a program to take a series of parameters say 3,45,6,9,10,34 and also a function and print the modified values. 
The function could be any arbitrary function.

'''
def arbitrary_func(x, y, z):    
    return f"x: {x}, y: {y}, z: {z}"

result3 = invoke_function(arbitrary_func, x=1, y=2, z=3) #Now in result3 it has arbitrary_func(x=1, y=2, z=3)

print(result3)  # Output: x: 1, y: 2, z: 3

def apply_function_to_parameters(func, *args):
    modified_values = [func(arg) for arg in args]
    return modified_values
'''
Task 5
Write a program to take a series of parameters say 3,45,6,9,10,34 and also a function and print the modified values. 
The function could be any arbitrary function.
'''
import types

def invoke_function(function, **kwargs):
    if isinstance(function, types.FunctionType):
        return function(**kwargs)
    else:
        print("Condition not match")


def arbitrary_func(x, y, z):    
    return f"x: {x}, y: {y}, z: {z}"

result3 = invoke_function(arbitrary_func, x=1, y=2, z=3) #Now in result3 it has arbitrary_func(x=1, y=2, z=3)

print(result3)  # Output: x: 1, y: 2, z: 3


#Main Function
def apply_function_to_parameters(func, *args):
    modified_values = [func(arg) for arg in args]
    return modified_values

# Example arbitrary functions, below 3 functions consider as Result Stored Functions
def square(x):
    return x * x
def add_ten(x):
    return x + 10
def double(x):
    return x * 2

# Example usage
parameters = [3, 45, 6, 9, 10, 34]

#Resultant Functions

modified_values_square = apply_function_to_parameters(square, *parameters)
print("Modified values (square):", modified_values_square)  # Output: [9, 2025, 36, 81, 100, 1156]

modified_values_add_ten = apply_function_to_parameters(add_ten, *parameters)
print("Modified values (add ten):", modified_values_add_ten)  # Output: [13, 55, 16, 19, 20, 44]

modified_values_double = apply_function_to_parameters(double, *parameters)
print("Modified Double Values:", modified_values_double) #output: [6, 90, 12, 18, 20, 68]


'''
Using Nested Functions
'''
# case 1
def outside():
    def inside(base,exponential):
        power = base **exponential
        return power
    return inside

variable= outside()
output = variable(2,3)
print(output)

# case 2
def func01():
    def add(a,b):
        return a+b
    return add

x=func01()
result = x(2,3)
print(result)

