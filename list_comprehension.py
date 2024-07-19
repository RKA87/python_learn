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


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

output=[element for element in fruits if "a" in element]

print("Fruits Lits with a letter:", output)

numbers = [1, 2, 3, 4]
squared_numbers=[number**2 for number in numbers]
print("Squared Numbers:",squared_numbers)

x=map(lambda number:number*2, numbers)
result=list(x)
print("Resultant list:",result)

twoDMatrix = [[10, 20, 30], 
              [40, 50, 60], 
              [70, 80, 90]]
print(twoDMatrix[1][2])

#list comprehension with function
def digitSum(n): 
    dsum = 0
    for ele in str(n): 
        dsum += int(ele) 
    return dsum 
  
# Initializing list 
List = [367, 111, 562, 945, 6726, 873]
output_result=[digitSum(i) for i in List if i & 1] #need to check with sir, if 1 & i
print(output_result)