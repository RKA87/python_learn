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


# vowel_count_list=[each_string for each_string in string_list for char in each_string if char in vowels] #need to check with sir 
# print(vowel_count_list) 

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

#case 2 comprehension list, need to check with sir
# result=[element for element in prices if str(element).startswith("-") or str(element)=="0" print "" else element]

