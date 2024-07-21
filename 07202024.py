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