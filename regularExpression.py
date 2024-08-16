'''
In regular expression it has search, findall, split & sub are the instance methods
findall - it gives characters as a output from the string
search -  it gives start, end & span of the index position from the string findings and it gives match object with span info as result
match - The re.match function only checks for a match at the beginning of the string
'''

'''
write a program to check the string contains only a certain set of characters (a-z,A-Z and 0-9)
'''
import re

def string_char_only(input_string):
    reg_expression=r'[a-zA-Z0-9]'
    output=re.findall(reg_expression,input_string)
    return output

input_string="ABCDEFabcdef123450"
result=string_char_only(input_string)
print(result)


'''
Search for the word "portal" in the given string
'''
s="GeeksforGeeks: A computer science portal for geeks"
exp=r"portal"
res=re.search(exp,s) #using findall will get to know 'portal' is exist & using search will get result as Match

print(res.start()) #it display's index start position of word "portal"
print(res.end()) #it display's index end  position of word "portal"
print(res.span()) #it display's index start to end position of word "portal"

string = "The quick brown fox jumps over the lazy dog"
pattern=r'[a-m]' #a set of characters pattern 
print(re.findall(pattern,string)) #since we are using findall, it display a-m characters only from the string

strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox'] 
reg_pattern=r'^T'
for each in strings:
    if re.match(reg_pattern,each):
        print("Matched Element:",each)
    else:
        print("Not Matched Element")


string1 = "Hello World!"
exp1=r'World'

print(re.findall(exp1,string1))
print(re.search(exp1,string1))
print(re.match(r'\bHel*',string1))

string2="The quick brown fox jumps over the lazy dog"
exp2=r"brown.fox" #here . reprsents any character

if (re.search(exp2,string2)):
    print("Exists")
else:
    print("Not Exist")

string3="Hanuman"
exp3=r'ra*'
if (re.match(exp3,string3)):
    print("Match")
else:
    print("Not Matched")

def text_match(text):
        patterns = 'z|Z'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))