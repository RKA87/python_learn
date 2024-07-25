# case 1
# Create a dictionary of squares of numbers from 1 to 10

dict_result={}
for i in range (1,11):
    dict_result[i] = i*i

print(dict_result)


dict_output={i:i*i for i in range(1,11)}
print(dict_output)

# case 2
# Create a dictionary of even numbers as keys and their squares as values

dict_even_squares={i:i*i for i in range(1,11) if i%2==0}
print("Dictionary Even Squares:", dict_even_squares)

# case 3
# dictionary of words and their lengths from a sentence
'''
Enter String : Python is awesome
{'Python': 6, 'is': 2, 'awesome': 7}
'''
x="Python is awesome"

y=(x.split(" "))

dict_output={}
for each in y:
    print(each, len(each))
    dict_output[each]=len(each)
    
print("Dictionary Output:",dict_output)

# case 4
# Create a dictionary of lowercase characters from a string
# Sample Output
# Hello World
# {'H': 'h', 'e': 'e', 'l': 'l', 'o': 'o', 'W': 'w', 'r': 'r', 'd': 'd'}

def string_output(element):
    string=element
    z=string.split(" ")

    joiner=""

    join_string=joiner.join(z)
    dictionary_output={each_char:each_char for each_char in join_string}

    return dictionary_output

x=string_output("Hello World")
print(x)

# 5. Create a dictionary of numbers and their cubes
# Sample Output
# [1, 2, 3, 4, 5]
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

def dict_cube(li):
    dict_output={each:each**3 for each in li}
    return dict_output

li=[1, 2, 3, 4, 5]
x=dict_cube(li)
print("Dictionary Output:",x)

# 6. Create a dictionary of numbers and their squares, excluding odd numbers
# Sample Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

def dict_squares(li):
    dictionary_even_squares={each_element:each_element**2 for each_element in li if each_element%2==0}
    return dictionary_even_squares

li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output=dict_squares(li)
print(output)

# 7. Create a dictionary of characters and their ASCII values from a string
# Sample Output
# Tutor Joes

def element_ascii(string_word):
    dict_output={each_element:ord(each_element) for each_element in string_word}
    return dict_output

string_word="Tutor Joes"
res=element_ascii(string_word)
print(res)

# 8. Create a dictionary of words and their vowels from a list of strings
# Sample Output
# ['apple', 'banana', 'cherry']
# {'apple': 2, 'banana': 3, 'cherry': 1}

def word_count(element):
    count=0
    for char in element:
        if char in "AaEeIiOoUu":
            count+=1
    return count

li=['apple', 'banana', 'cherry']
dict_output={element:word_count(element) for element in li}
print(dict_output)

# 13. Create a dictionary of words and their reversed forms
# Sample Output
# ['apple', 'banana', 'cherry']
# {'apple': 'elppa', 'banana': 'ananab', 'cherry': 'yrrehc'

li=['apple', 'banana', 'cherry']
dict_output={each:each[::-1] for each in li}
print(dict_output)
