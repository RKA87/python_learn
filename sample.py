# Task 2
# You are required to create a stop watch that displays the elapsed time in the 
# format MM:SS that stops after a certain condition is met (say when the count reaches 100).

# inp = int(input("Enter Counter Input:"))
# counter = 0
# for i in range(inp,0,-1):
#     counter +=1
#     if i != 100:
#         print("Time Format:", i,counter)

# kilometer_cost = 15

# journey_time_hours = int(input("Enter the total journey time which include break covers during travel:"))

# total_kilometers = int(input("Enter total kilometers:"))

# if journey_time_hours < 2:
#     trip_charges = kilometer_cost*journey_time_hours
#     print("Total Kilometers:", total_kilometers)
#     print("Journey Time Duration:", journey_time_hours)
#     print("Total Trip Charges:", trip_charges)

# if journey_time_hours>=2:

#     waiting_charge = 5
#     waiting_charge_input = int(input("Enter Waiting Charge in Minutes:"))
#     total_Waiting_charges = (waiting_charge_input*5)

    


#     break_charges = 5
#     break_charge_input = int(input("Enter break charges in mts:"))
#     total_break_charges = (break_charges*break_charge_input)

# x=[]
# for i in range(2,11,2):
#     x.append(i)

# print(len(x)-1)

# for i in range(2,10,2):
#     x.append(i)
# print(len(x))

# tot_journey = 0
# brk = 0.5
# count = 0
# for i in range(2,13,2):
#     tot_journey = tot_journey + 2 + brk
#     print(tot_journey)
#     if tot_journey < 13:
#         count +=1
#         print(count)

'''
Task 3:

Write a program to calculate the fare for each station from the given data.
Fare is calculated using the formulate distance * cost. 
The cost is given in an an array like so 200, 350, 55, 724, 120
The distance for each station is given in the dictionary below
{
“Delhi" : 650,
“Kolkata" : 700,
“Mumbai" : 625,
“Chennai" : 400,
“Pune" : 600
}

Use *args and **kwargs as function parameters
'''
# cost_list =[200,350,55,724,120]

# distance={
#     "Delhi": 650,
#     "Kolkata": 700,
#     "Mumbai": 625,
#     "Chennai": 400,
#     "Pune": 600
# }

# empty_list = []

# for val in distance.values():
#     empty_list.append(val)

# distance_cost_result=[]

# for i in range(0,len(cost_list)):
#     x= empty_list[i]*cost_list[i]
#     distance_cost_result.append(x)
# print(distance_cost_result)

# x=[]
# for key in distance.keys():
#     x.append(key)

# final_result_dictionary={}
# for i in range(len(x)):
#     final_result_dictionary[x[i]]=distance_cost_result[i]

# print(final_result_dictionary)

# Task 9

# Write a program to calculate the sum of a list of numbers using recursion.


# number = 100

# def times(n1,n2):
#     result = n1**n2 #** power function
#     return result

# def compute(fn, n1, n2):
#     return fn(n1,n2)

# print(compute(times, 1,2))
# print(compute(times, 2,3))
# print(compute(times, 2,2))


# def power_function():
#     def calculate_power(x,y):
#         return x**y
#     return calculate_power

# result = power_function()
# print(result(3,3))

#case
# def fun02(arg4):
#     return arg4

# def fun01(fn,*args):
#     return fn(*args)

# x=[2,3,4]
# testing = fun01(fun02,x) #fun02(x)

#case create an inner function to calcuate the addition
'''
Task 16
Given a Python list, write a program to remove all occurrences of a given item.
[2,3,4,1,2,5,10,2] remove 2..
'''

# li=[2,3,4,1,2,5,10,2]
# num = 2

# for each in li:
#     if num == each:
#         li.remove(each)
# print(li)


# l1=["rakeh", "suji", "ram", "sita", "suji"]

# input_string = "suji"

# for each in l1:
#     if each == input_string:
#         l1.remove(each)
# print(l1)

# l=[1,4,5,19,0, 23, -1, 45]
# min1=l[0]
# for i in range(len(l)):
#      # If the other element is min than first element
#     if l[i] < min1:
#         min1 = l[i] #It will change

# print("The smallest element in the list is ",min1)

# x=l[0]
# for element in l:
#     if element <= x:
#         x=element
# print("Smallest Element is:", x)
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *
# x="*"
# for row in range(6,0,-1):
#     for col in range(6):
#         if col < row:
#             print(" ", end=" ")
#         else:
#             print(x, end=" ")
#     print(" ")

# names = ['david', 'peter', 'jenifer']

# def capitalize(name):
#     return name.capitalize()

# res=map(capitalize,names)
# print(list(res))

# res=map(lambda name:name.capitalize(), names)
# print(list(res))


# Find the largest number in the list [1,4,5,19,0, 23, -1, 45]
# Find the smallest number in the list [999,12,34,111,-7,-11,45]

# Task 7:
# Given two arrays, find all pairs from both arrays whose sum is equal to x. 
# Input : arr1 = [1, 2, 4, 5, 7] ; arr2 = [5, 6, 3, 4, 8]  
# x = 9
# Output : [(1, 8), (4, 5), (5, 4)]

  

# for x in arr1:
#     for y in arr2:
#         if x + y == 9:
#             print(x,y)

# Task 20
# Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
# import timeit

# def test():
#     list_comprehension=[number for number in range(1200,2000,130)]

# print(timeit.timeit(stmt='[number for number in range(1200,2000,130)]'))

# Task 10:
# You have a list of prices - replace negative prices with 0 and leave the positive values unchanged:
# prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# Result = [1.25, 0, 10.22, 3.78, 0, 1.26]
# given_list=['apple', 'banana', 'cherry']
# result_list=[]

# vowels="AaEeIiOoUu"
# for word in given_list:
#     for char in word:
#         if char in vowels:
#             word=word.replace(char, "*")
#     result_list.append(word)
# print("Input Given List:", given_list)
# print("Asterik List Result:",result_list)


import timeit

# list_comprehension=[number for number in range(1200,2000,130)]
# new_list=timeit.timeit(stmt=list_comprehension)
# print(new_list)

# lambda_function=lambda number:number in range(1200,2000,130)
# lambda_list=timeit.timeit(lambda_function)
# print(lambda_list)

def add_six():
    new_list=[number+6 for number in range(1,100)]
    return new_list

# 8. Create a dictionary of words and their vowels from a list of strings
# Sample Output
# ['apple', 'banana', 'cherry']
# {'apple': 2, 'banana': 3, 'cherry': 1}
# sentence = "Python is fun"

# x=(sentence.split()[::-1])
# print(list(enumerate(x)))

list_d = [
    {"Full Throttle": 1995},
    {"Sid Meier's Civilization II": 1996},
    {"Diablo": 1996},
]

res={}
for d in list_d:
    res.update(d)

print(res)

res2={key:value for d in list_d for key,value in d.items()}
print(res2)

# using condition statement only 1996

res3={key:value for d in list_d for key,value in d.items() if value==1996}
print(res3)
