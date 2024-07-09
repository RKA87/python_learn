'''
Task 1
Find the largest number in the list [1,4,5,19,0, 23, -1, 45]
'''
def large_number(parameter1):
    x=parameter1
    x.sort()
    print("After Sorting, List Output:", x)
    res=len(x)-1
    print("Largest Number from given list:", x[res])

parameter1= [1,4,5,19,0, 23, -1, 45]
large_number(parameter1)

'''
Task 2
Find the smallest number in the list [999,12,34,111,-7,-11,45]
'''
def smallest_number(parameter2):
    y=parameter2
    y.sort()
    print("After Sorting, List Output:", y)
    print("Smallest Number from given list:", y[0])

parameter2= [999,12,34,111,-7,-11,45]
smallest_number(parameter2)

'''
Task 3
Find the sum of squares of the numbers of the list [2,3,11, 21, 8, 10, 6]
'''
def sum_squares_val(parameter3):
    x=parameter3
    var1=0
    for each in x:
        temp=each*each
        var1 += temp
    print("Sum of Squares of the given numbers in the list:", var1)

parameter3=[2,3,11, 21, 8, 10, 6]
sum_squares_val(parameter3)

'''
Task 4
Extend the above program to find the count of elements that are divisible by 10 (square of numbers)
'''
def squared_val_divisible(parameter3):
    x=parameter3
    var1=0
    for each in x:
        temp_number=each*each
        if temp_number%10==0:
            print("After Squared the Number, Value is:", temp_number)
            print("It is Divisible by 10", '\n')
        else:
            print("from Squared the Number, value is {} and it is not divisible by 10 ".format(temp_number),'\n')
parameter3=[2,3,11, 21, 8, 10, 6]
squared_val_divisible(parameter3)
'''
Task 5
Find the sum of the odd elements of the list [2,34,11,15, 23,8,9,11]
'''

def sum_odd_elements(parameter5):
    elements = parameter5
    sum_odd_numbers = 0
    for each_element in elements:
        if (each_element%2) !=0:
            sum_odd_numbers += each_element
    print("Total Sum of Odd Elements:", sum_odd_numbers)

parameter5=[2,34,11,15,23,8,9,11]
sum_odd_elements(parameter5)

'''
Task 6
You are given a list [1,2,3,4,5,6,7,8,9,10].  
Print the sum of the elements as shown below. 
The sum of the first element and the last element, the sum of second element and the last but one element and so on..

1 + 10 = 11
2 + 9 = 11
3 + 8 = 11
'''
def sum_elements(arg):
    l = arg
    for i in range(len(l)):
        x = (l[i]+l[-i-1])
        print(l[i], "+", l[-i-1], "=", x)

l=[1,2,3,4,5,6,7,8,9,10]
sum_elements(l)

'''
Task 7
You are given 2 lists.  
Compare the elements of the list and print the greatest of the 2 for each element.  
Ex. 2 > 1, Print 2, 45 > 34 print 45.  Repeat this for every element of the list 
[2, 34, 5, 7, 10, 13] 
[1,45, 6, 7, 11, 14]
'''

def greater_number(l1,l2):
    x=l1
    y=l2
    for i in range(0,len(x)):
        if x[i] > y[i]:
            print(x[i], ">", y[i], "=", x[i] )
        else:
            print(x[i], ">", y[i], "=", y[i])

l1=[2, 34, 5, 7, 10, 13] 
l2=[1,45, 6, 7, 11, 14]

greater_number(l1,l2)

'''
Task 8
Divide the elements of the list by 2 and display the result
[21, 3, 15, 72, 9, 24, 45]
'''
def divide_by_2(l):
    x= l
    for each in l:
        res=each/2
        print(each,"/2", "=", res)

l=[21, 3, 15, 72, 9, 24, 45]

divide_by_2(l)
'''
Task 9 
The marks of a student for all the subjects of a semester is given in an array [23, 45, 50, 49, 12, 33, 17, 40]

The following needs to be printed

The average marks - (total sum of elements in list/total no of elements)
The least marks - find the min element
The maximum marks - find the max element

Grade for each subject as per the following
If marks < 15, Grade - C
If marks is between 15 and 35 Grade - B
If marks is above 35, Grade - A

Print the count of subjects that have A, B and C grades.
If there are a minimum of 4 As, the student is declared passed.
'''

def tot_sum(arg):
    tot=0
    for element in arg:
        tot += element
    return tot

def avg_marks(arg):
    avg_marks = tot_sum(arg)/len(arg)
    return avg_marks

def least_marks(arg):
    least_marks = min(arg)
    return least_marks

def max_marks(arg):
    max_marks = max(arg)
    return max_marks

def grades(arg):
    grade_a_count = 0
    grade_b_count = 0
    grade_c_count = 0

    for subject in arg:
        if (subject < 15):
            grade_c_count +=1
        elif (subject >=15 and subject <35):
            grade_b_count +=1
        elif (subject > 35):
            grade_a_count +=1
    return grade_a_count, grade_b_count, grade_c_count

def student_report(arg):

    print("Average Marks:",avg_marks(arg))
    print("Least Marks:",least_marks(arg))
    print("Maximum Marks:",max_marks(arg))

    (x,y,z) = grades(arg)
    print("Count of Grade A:",x)
    print("Count of Grade B:",y)
    print("Count of Grade C:",z)

    if x>4:
        print("Student Declared Pass")
    else:
        print("Student not met Pass Criteria")

arg = [23, 45, 50, 49, 12, 33, 17, 40, 75]
student_report(arg)
'''
Task 10
A business has a strange way of calculating the commissions offered to the clients  at 10%. 
The calculation is done as under:
unit sales = [10,200,30,26,65,75]

Commission calculation
(10+200)/2 = 210/2  = 105
(200+30)/2 = 230/2 = 115
(30+26)/2 = 56/2 = 28
(26+65)/2 = 91/2 = 45
(65+75)/2 = 140/2 = 70

The commission percentage is calculated by adding all the numbers above like 105+115 +28+45+70 / 5  = 72
Commission is 72 * 10/100 = 7.2 

Write a program to calculate the commission as indicated above.
'''
def calculating_commission(unit_list):

    final_res=0
    counter=0
    for i in range(0,len(unit_list)-1):
        res = unit_list[i]+unit_list[i+1]
        print(unit_list[i],"+", unit_list[i+1],"=", res)
        y=res/2
        counter +=1
        final_res = final_res+y
    print("Commission Percentage Calculate by add all outcomes:", final_res/counter)
    commission_percentage = (final_res/counter)*10/100
    return commission_percentage

unit_sales = [10,200,30,26,65,75]
commission_percentage=calculating_commission(unit_sales)
print("Commission Percentage =", commission_percentage)
'''
Task 11
A list contains the names of the fruits - [“mango”, “papaya”, “citrus”, “guava”, “pomegranate”, “apricot”, “apple”, “pineapple”]  
Write a program to display the fruit that has the least number of letters and the maximum number of letters along with the name of the fruit. 
'''
def min_max_fruit(list1):
    l2=[len(each) for each in l1]

    min_len=min(l2)
    max_len=max(l2)

    for each in list1:
        if len(each) == min_len:
            print("Min Value:",min_len,"Fruit Name:", each)

    for each in list1:
        if len(each) == max_len:
            print("Max Value:",max_len,"Fruit Name", each)

l1=["mango", "papaya", "citrus", "guava", "pomegranate", "apricot", "apple", "pineapple"]
min_max_fruit(l1)
'''
Task 12
Write a program to check if the letters of the list follow the palindrome.. 
['m','a','d','a','m']
'''
x=['m','a', 'd', 'a', 'm']
count=0
for number in range(0,len(x)):
    if x[number] == x[-number-1]:
        count = count+1

print("Value of Count:", count)

if count == len(x):
    print("Its a Palindrome")
else:
    print("Given input string is not a palindrome")
'''
Task 13
You are given 2 lists.  Concatenate the elements of the list index wise

[“yellow”, “red”, “green”, “white”, “blue”, “brown”]
[“mango”, “apple”, “guava”, “musk melon”, “Blue berries”, “kiwi”]

Output should be like mango - yellow, etc..
'''
l1= ["yellow", "red", "green", "white", "blue","brown"]
l2= ["mango", "apple", "guava", "musk melon", "Blue berries", "kiwi"]

for element in range(0,len(l2)):
    print(l2[element],"-",l1[element],"",end = "")

'''
Task 14
Remove empty strings from a list of strings like [“Jupiter”, “”, “venus”, “Mars”, “”, “earth”, “Neptune”]
'''

def remove_empty_string(li):

    output_li = []
    for each in li:
        if len(each) > 0:
            output_li.append(each)
    return output_li

input_li=["Jupiter", "", "venus", "Mars", "", "earth", "Neptune"]    

res = remove_empty_string(input_li)

print(res)
'''
Task 15
You have given a Python list. 
Write a program to find the value of an item in the list, and if it is present, replace it with another item. Only update the first occurrence of an item.
[1, 3, 16, -1, 0, 9, 200, 3]

Example replace - 0 with 20.  

Use functions
'''
def replace_first_entry(num):

    li=[1, 3, 16, -1, 0, 9, 200, 3]
    input_number = num

    if input_number in li:
        print("number exist")
        li[li.index(input_number)]=27

    return li

x = 200
res=replace_first_entry(x)
print("Result List:", res)
