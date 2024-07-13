'''
For lambda, make sure to lambda output:logic, input

for map function follows syntax is map(function,input)

for filter function follows sysntax is filter(function,input)

here function can be called as lambda

map or filter functions you can call any iterable functions
'''
def addition(n):
    return n+n

numbers=(1,2,3,4)

res=map(addition, numbers)
print(list(res))

#using lambda function
res=map(lambda n:n+n, numbers)
print(tuple(res))

names = ['david', 'peter', 'jenifer', 'suji', 'rakesh']

def capitalize(name):
    return name.capitalize()

res=map(capitalize,names)
print(list(res))

res=map(lambda name:name.capitalize(), names)
print(tuple(res))

carts = [['SmartPhone', 400], ['Tablet', 450], ['Laptop', 700]]

def increased_val(item):
    item[1]=item[1]*100 #here list is pass by reference so in a list items will get auto update
    return item

result=map(increased_val,carts)
print("Using map function:",tuple(result))

#using lambda function
result=map(lambda item:item[1]+100,carts) #here result stores only in a carts list each item,item->list->printing item[]
print("Using lambda function output:",list(result))
print("Final Output of Carts:", carts)

#Passing two lists at a time using map & lambda fucntions
list1=[1,3,5,7]
list2=[2,4,6,8]

def two_list_function(x,y):
    return x+y

result=map(two_list_function, list1,list2)
print("Two List Function Numbers Output:",list(result))

result=map(lambda x,y:x+y, list1,list2)
print("Using lambda function output:", tuple(result))

#even numbers check

def even_num(number):
    if number%2==0:
        return number*2
    else:
        return number
    
numbers=[2,3,4,5,6,7,8]
result=map(even_num,numbers)
print("Using map function:", tuple(result))

#using lambda function
result=map(lambda number:number*2 if number%2==0 else number, numbers) #lambda logic to be observe (if & else condition)
print("Uing lambda function:",list(result))


###########################################################
# FILTER FUNCTIONS
###########################################################
ages = [5, 12, 17, 18, 24, 32]

def my_age(x):
    if x > 18:
        return x
    else:
        return False
    
res=filter(my_age,ages) #filter will automatically filter the elements and it won't store like map funtion (all elements)
print(list(res))

#Using lambda function

res=filter(lambda age:age>18, ages)
print("Using lambda function output:", tuple(res))
