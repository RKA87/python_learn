my_list=[2,3,4,5,7,8,9,10]
even_odd=[True if x%2==0 else False for x in my_list]
print(even_odd)

squared_list=[x**2 for x in my_list]
print("Squared List:", squared_list)

#pass fail labels if greater than 70
score=[64,75,74,83,57,76,67,82]
pass_fail=["Pass" if x >= 70 else "Fail" for x in score]
print(pass_fail)

#adding two lists
x=[64,75,74,83,57,76,67,82]
y=[82, 67, 76, 57, 83, 74, 75, 64]

add=[element1+element2 for element1,element2 in zip(x,y)]
print("Addtion Output:", add)

odd_number=[f"Odd Number - {x}" for x in my_list if x %2 !=0]
print(odd_number)

concatenated_list=x+y
print("Concatenated List Output:", concatenated_list)