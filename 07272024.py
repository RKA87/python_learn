'''
Task 1 
Find the difference between 2 lists

elements that are not common in both lists
'''
# case 1

l1=['foo', 'bar', 'baz', 'qux','Smith','McArthur']
l2=['Smith', 'McArthur', 'Wilson', 'Johansson','bar', 'baz']

x=[element for element in l1 if element not in l2]

y=[element for element in l2 if element not in l1]

print("Not Common Elements from Both Lists:", x + y)

# case 2

l1_not_in_l2=set(l1).difference(l2)
print(l1_not_in_l2)

l2_not_in_l1=set(l2).difference(l1)
print(l2_not_in_l1)

'''
Task 2
Common Elements of 3 lists using sets
'''

l4 = ["ram", "sita", "lakshman", "lakshman"]
l5 = ["hanuman", "vali", "sugriva","hanuman"]
l6 = ["Raj", "Billy", "Aravind", "Billy"]

output=set(l4).union(set(l5),set(l6))
print("Output of 3 Lists Using Sets:", output)

'''
Set with string
'''
string="rakeshkumar"

print(set(string))

'''
Keep ONLY the duplicates - common elements of sets 
sets intersection method you can use "&" or "intersection"
The intersection() method will return a new set, that only contains the items that are present in both set
'''
s1 = {"apple", "banana", "cherry","techM"}
s2 = {"google", "techM","microsoft", "apple"}
s3 = {"google", "techM", "apple"}

intersection_set=s1&s2 # s1.intersection(s2)
# print(intersection_set)

intersection_output=s1&s2&s3
print(intersection_output)

'''
Task 3
count no of vowels in a given string using sets
'''
string="rakeshkumar"
vowels="aAeEiIoOuU"

no_of_vowels=[element for element in string if element in vowels]
print("No of Vowels in String:",len(no_of_vowels))

# After Conversion, using Set

set_string=set(string)

set_string_no_of_vowels=[element for element in set_string if element in vowels]
print("No of Vowels in String, After convert into Set:",len(set_string_no_of_vowels))

'''
Task 4
check if set is a superset of itself or another given set
'''
def subset(s1,s2):
    set1=s1
    set2=s2
    if s1.issuperset(s2):
        return ("set1 is superset of set2")
    else:
        return ("set1 is not superset of set2")


set1={"Rakesh", "Ram", "Rajesh","lakshman", "Hanuman"}
set2={"Rakesh", "Ram", "Rajesh"}
set3={1,2,3,4,5}

result=subset(set2,set3)
print(result)

'''
Task 5
Get intersection of two lists using sets
'''
l7=["Rakesh", "Ram", "Rajesh","lakshman", "Hanuman"]
l8=["Rakesh", "Ram", "apple", "cherry", "banana"]

intersection_result=set(l7).intersection(set(l8))
print("Intersection result:",intersection_result)

'''
Task 6
Determine if two sets are disjoint or not
Disjoint: If they have no common elements between two sets is Disjoin
'''
def disjoint_or_not(x,y):

    set1=x
    set2=y
    try:
        if set1.isdisjoint(set2):
            return ("No Common Elements between two sets")
        else:
            return ("Common Elements exist between two sets")
    except Exception as E:
        return ("Error:",E)

s5={"Rakesh", "Ram", "apple", "cherry", "banana"}
s6={"dragon fruit"}
disjoint_result=disjoint_or_not(s5,s6)
print(disjoint_result)

'''
Task 7
write a program to remove the given items for a set at once
'''
def remove_set_elements(set_input,list_input):
    res=[set_input.remove(element) for element in list_input if element in set_input]
    return set_input

s7={"Rakesh", "Ram", "apple", "cherry", "banana"}
elements=["Rakesh", "Ram","lamp", "tiger"]

result=remove_set_elements(s7,elements)
print("After Elements Removed from Set:",result)

