# Task 1:
# The heights of the students are given in an array, h = [123, 150, 180, 160, 150, 175].  
# Write a program to determine the average of the heights using List Comprehension. 

# case 1
def sum_height(height_list):
    sum = 0
    for each in height_list:
        sum = sum + each
    return sum
    
height_list=[123, 150, 180, 160, 150, 175]
result = sum_height(height_list)
avg_height = result/len(height_list)
print("Average Height:",avg_height)

# case 2
sum_list=sum(number for number in height_list)
avg=(sum_list/len(height_list))
print("Average Height:", avg)

# Task 2:
# Write a program to return the part of the elements of the given list using list comprehension

# Eg. l = [50, 23, 100, 9, 81, 25] 
# Result = [25, 11, 10, 4, 40, 12]	
# The fraction and the list should be parameters to the function. 

def fraction_result(l,fraction_number):
    fraction_result=[each_element/fraction_number for each_element in l]
    split_fraction=[str(number).split(".")[0] for number in fraction_result]
    return split_fraction

l = [50, 23, 100, 9, 81, 25] 
fraction_resultant_list = fraction_result(l,3)
print(fraction_resultant_list)

# Task 3:
# Write a program to find the count of vowels in each element of the list.  Ex. colors = [“white”, “brown”, “yellow”, “green”, “orange”]  
# Result = [2, 1, 2, 2, 3]	#lists the count of vowels in each 

# case 1
def char_count(each_word):
    vowels="AaEeIiOoUu"
    count=0
    for char in each_word:        
        if char in vowels:
            count +=1
    return count

string_list=["white","brown","yellow","green","orange"]
vowel_count_list=[char_count(each_word) for each_word in string_list]
print(vowel_count_list)

#case2

def vowel_count_list(list):

    vowels = "AaEeIiOoUu"
    count_list = []
    for each_string in list:
        count=0
        for each_char in each_string:
            if each_char in vowels:
                count +=1
        count_list.append(count)
    return count_list

string_list=["white","brown","yellow","green","orange"]
result_list=vowel_count_list(string_list)
print("Vowels Count List of Each String in List:",result_list)

# Task 4
# Get details about the __hash__ property in python

class MyClass:
    def __hash__(self):
        pass

obj=MyClass()
print(dir(obj))

# Task 5:
# Given a list of months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# Write a program to:
# Return those months that end in ‘y’
# Return those months whose length is > 6
# Return the months in Capital letters

def finding_character(li):
    find_character_element = [element for element in li if element[len(element)-1] == "y" ]
    return find_character_element

def month_length(li):
    month_length_list=[element for element in li if len(element)>6]
    return month_length_list

def month_capital(li):
    month_captial_letters=[element.upper() for element in li]
    return month_captial_letters

x=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

res1=finding_character(x)
print("Months that end in y:",res1)

res2=month_length(x)
print("Months Lenght Greater than 6:",res2)

res3=month_capital(x)
print("Months list in Upper Case:",res3)

# Task 6:
# Use the enumerate method to display the index and value of the items of the 
# list months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def enumerate_list(li):
    list_output=[(index,value) for index,value in enumerate(li)]
    return list_output

months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
output=enumerate_list(months_list)
print("Enumerate Results:",'\n',output)


# Task 7:
# Given two arrays, find all pairs from both arrays whose sum is equal to x. 
# Input : arr1 = [1, 2, 4, 5, 7] ; arr2 = [5, 6, 3, 4, 8]  
# x = 9
# Output : [(1, 8), (4, 5), (5, 4)]

def resultant_list(l1,l2):
    list_output=[]
    for x in l1:
        for y in l2:
            if x+y==9:
                output=(x,y)
                list_output.append(output)
    return list_output

arr1 = [1, 2, 4, 5, 7]
arr2 = [5, 6, 3, 4, 8]
output=resultant_list(arr1,arr2)
print(output)

# Task 8:
# Using list comprehension, write a program to return the first ten perfect squares.

def ten_square_list():
    list_output=[element**2 for element in range(1,11)]
    return list_output

output=ten_square_list()
print("First Ten Square Output:",output)

# Task 9:

# Write a program to return the consonants in the lists.

# Eg. sentence = ("The rocket, who was named Ted, came back", "from Mars because he missed his friends.")
# Output 
# ['T', 'h', 'r', 'c', 'k', 't', 'w', 'h', 'w', 's', 'n', 'm', 'd',
#  'T', 'd', 'c', 'm', 'b', 'c', 'k', 'f', 'r', 'm', 'M', 'r', 's', 'b',
#  'c', 's', 'h', 'm', 's', 's', 'd', 'h', 's', 'f', 'r', 'n', 'd', 's']
def consonants_list(x):
    vowels="AaEeIiOoUu,. "
    outpt_list=[char for element in x for char in element if char not in vowels]
    return outpt_list

sentence="The rocket, who was named Ted, came back", "from Mars because he missed his friends."
consonants_output=consonants_list(sentence)
print("Consonants List Output:",'\n',consonants_output)

# Task 10:
# You have a list of prices - replace negative prices with 0 and leave the positive values unchanged:
# prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# Result = [1.25, 0, 10.22, 3.78, 0, 1.26]
def res(l):
    result=[]
    for element in l:
        x=str(element)
        if x.startswith("-"):
            replace_value="0"
            result.append(replace_value)
        else:
            result.append(element)
    return result

prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
output=res(prices)
print("Prices Input List:",prices)
print("Output Result List:",output)

def element_conversion(element):
    x=str(element)
    if x.startswith("-"):
        x="0"
    else:
        x
    return x

prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
result_list=[element_conversion(element) for element in prices]
print(result_list)

# Task 11:
# Generate a list of tuples containing a number and its square.
# [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

def tup_range(number):
    new_list=[(x,x*x) for x in range(1,number)]
    return new_list

num=7
res=tup_range(num)
print("List of Tuple set using the Number:",res)

# Task 12:
# Create a list of even numbers squared and odd numbers cubed from 1 to 10
# [1, 4, 27, 16, 125, 36, 343, 64, 729, 100]

for i in range(1,11):
    if (i%2)==0:
        print(i*i)
    else:
        print(i**3)

def square_cube(number):
    square_cube_list=[i**2 if (i%2==0) else i**3 for i in range(1,number)]
    return square_cube_list

x=11
res=square_cube(x)
print("Square Cube List:",res)

# Task 13:
# Create a list of first characters from a list of words
# ['apple', 'banana', 'cherry']
# ['a', 'b', 'c']
def first_char(li):
    new_list=[ element[0]  for element in li]
    return new_list

li=['apple', 'banana', 'cherry']
res=first_char(li)
print("First Character from list:",res)

# Task 14:
# Create a list of strings with vowels replaced by asterisks
# Sample Output
# ['apple', 'banana', 'cherry']
# ['*ppl*', 'b*n*n*', 'ch*rry']

given_list=['apple', 'banana', 'cherry']
result_list=[]

vowels="AaEeIiOoUu"
for word in given_list:
    for char in word:
        if char in vowels:
            word=word.replace(char, "*")
    result_list.append(word)
print("Input Given List:", given_list)
print("Asterik List Result:",result_list)

# case 2
def asterik_list(li):    
    result_list=[''.join('*' if char in "AaEeIiOoUu" else char for char in element) for element in li]
    return result_list

given_list=['apple', 'banana', 'cherry']
output=asterik_list(given_list)
print(output)

# case 3
def astreik_output(element):
    vowels="AaEeIiOoUu"
    for each_char in element:
        if each_char in vowels:
            element=element.replace(each_char, "*")    
    return element

output=astreik_output("apple")
print(output)

given_list=['apple', 'banana', 'cherry','rakesh', 'sujana']
res=[astreik_output(element) for element in given_list]
print(res)

# Task 15:
# Create a list of characters that are digits from a string
# Sample Output
# 12345Hello67890
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

string="12345Hello67890"
# case 1
new_list=[]
for each_element in string:
    if each_element.isdigit():
        new_list.append(each_element)
print(new_list)

# case 2
def string_list(string):
    new_list=[each_element for each_element in string if each_element.isdigit()]
    return new_list

result=string_list(string)
print("Resultant List:",result)

# Task 16
# Given a list of numbers, remove floats (numbers with decimals)

# case 1
original_list = [2,3.75,.04,59.354,6,7.7777,8,9]
filtered_list=[]
for element in original_list:
    if type(element) is float:
        pass
    else:
        filtered_list.append(element)

print(original_list)
print(filtered_list)

# case 2
def remove_float(li):
    new_list=[element for element in li if type(element) is not float]
    return new_list

filter_list=remove_float(original_list)
print("After float elements removed:",filter_list)

# Task 17
# Find all the numbers from 1-100 that are divisible by 7

def divisible_by_7():
    new_list=[element for element in range(1,101) if element%7==0]
    return new_list

output=divisible_by_7()
print("7 Divisible List:",output)

# Task 18
# Find all the numbers from 1-100 that have 3 in them

# case 1
for num in range(1,41):
     x=str(num)
     if x.endswith("3") or x.startswith("3"):
          print(x)

# case 2
def three_in_list(number):
     new_list=[str(num) for num in range(1,number) if str(num).startswith("3") or str(num).endswith("3")]
     return new_list

three_list=three_in_list(101)
print("Numbers that have 3 list:",three_list)

#Task 19
# Count the number of space in a string
# Ex. “H ll  W rld”

example="H ll  W rld"
example2="R a K E s H"
print(example2.count(" "))

# Task 20
# Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
def steps_130(number_range):
    new_list=[number for number in range(1200,number_range,130)]
    return new_list

x=steps_130(2000)
print("steps 130 difference list:",x)

# Task 21
# Use list comprehension to construct a new list but add 6 to each item
def add_six():
    new_list=[number+6 for number in range(1,100)]
    return new_list

output=add_six()
print("Add Six for Every Element List:",output)


# Task 22
# Timeit is a package that provides a timer function.. The details can be learnt at https://docs.python.org/3/library/timeit.html
# Use timeit to prove that list comprehension is faster compared to map and for loop using any of the problem given above. You can consider using Task 20

# need to check with Sir
import timeit
'''
syntax:

The timeit module expects a statement that can be executed. You should either pass a full expression or function call
'''
print(timeit.timeit(add_six))

