# Add an item to the set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)

# Adding the set into existing set using update

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# Adding two sets using union
set1 = {"ram", "sita", "lakshman"}
set2 = {"hanuman", "vali", "sugriva"}
set3 = {"Raj", "Billy", "Aravind"}

c=set1.union(set2,set3)
print("Joined Sets:",c)

'''
Count the number of vowels in given a string using sets
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

def disjoint_or_not(x,y):

    try:
        set1=x
        set2=y
        if (type(set1)) and (type(set2)) == "set":
            return ("Given Input is set Datatype")
        else:
            raise Exception
    except Exception as E:
        return ("Given Input is not in set datatype")
    # if set1.isdisjoint(set2):
    #     return ("No Common Elements between two sets")
    # else:
    #     return ("Common Elements exist between two sets")
    
s4={"Rakesh", "Ram", "Rajesh","lakshman", "Hanuman"}
s5={"Rakesh", "Ram", "apple", "cherry", "banana"}
disjoint_result=disjoint_or_not(s4,s5)
print(disjoint_result)

