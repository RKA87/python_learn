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
def fun02(arg4):
    return arg4

def fun01(fn,*args):
    return fn(*args)

x=[2,3,4]
testing = fun01(fun02,x) #fun02(x)

#case create an inner function to calcuate the addition




def name(name,age):
    print(name, age)

name("rakesh", 27)

new_name= name
new_name("suji", 33)

tup = (223,"string", "string1", 485, 95, "set")


thisset = {"apple", "banana", "cherry", True, 1, 2}

thistuple = ("apple", "banana", "cherry")


y=list(thistuple)

y.remove("apple")
print(y)

thistuple = tuple(y)

print(thistuple)

#for unpacking the tuple
thistuple = ("apple", "banana", "cherry")

(green, yellow, orange) = thistuple

print(green)
print(yellow)
print(orange)

#it returns the value of index for a particular element
print(thistuple.index("banana"))


# if you want to modify the set & tuple you must convert into list and update it and again convert back to their data type
