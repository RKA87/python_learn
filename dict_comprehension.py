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