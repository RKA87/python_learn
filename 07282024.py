'''
Task 1
Find the difference between 2 lists.  
I.e.., elements that are not common in both lists. 
'''
l1=["apple", "banana", "cherry", "apple", "Uncle"]
l2=["Jay", "Idrish", "Archi", "cherry", "Rakesh"]

# converting into sets
s1=set(l1)
s2=set(l2)

#Elements that not are not common in both sets, which is difference
s1_not_in_s2=s1.difference(s2)
s2_not_in_s1=s2.difference(s1)

#Final Output set of different elements from both lists or sets
s3=s1_not_in_s2.union(s2_not_in_s1)

print("Final Set of Difference Elements from both sets:"'\n',s3)
'''
Task 2
Find common elements of Three given lists using Sets. 
'''
l3=["Rakesh", "Raj","Bryan","Mohan","Sundar","Ram"]
l4=["Ram", "Sita","Hanuman", "Lakshman","Sundar","Raj","Rakesh"]
l5=["Kumar", "Mercy", "Mary","Mark","Suji","Rakesh","Ram"]

s3=set(l3)
s4=set(l4)
s5=set(l5)
common_elements_set=s3&s4&s5 # | common elements from 3 sets using intersection "&"
print("Common Elements Set:",'\n',common_elements_set)

'''
Task 3
Count the number of Vowels in a given string using Sets
'''
input_string="rakeshkumarakuluru"

set_string=set(input_string)
vowels="AaEeIiOoUu"

no_of_vowels=[element for element in set_string if element in vowels]
print("Count of Vowels from input string:",len(no_of_vowels))

'''
Task 4
Check if a set is a superset of itself or another given set
'''

'''
Task 5
Get intersection of 2 lists using sets
'''
l6=["Ram", "Sita","Hanuman", "Lakshman","Sundar","Raj","Rakesh"]
l7=["Kumar", "Mercy", "Mary","Mark","Suji","Rakesh","Ram"]

output=set(l6) & set(l7)
print(output)

'''
Task 6
Write a program to determine if two sets are disjoint or not?
Disjoint: Two sets are disjoint if they have no elements in common
'''
def disjoint_set(set1,set2):
    x=set1
    y=set2
    try:
        if x.intersection(y):
            return ("True")
        else:
            return ("No Common Elements")
    except Exception as Error:
        return ("Error:",Error)

set1=["apple", "banana", "cherry"]
set2={"ram","sita"}

result=disjoint_set(set1,set2)
print(result)


