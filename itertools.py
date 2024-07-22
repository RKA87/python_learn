import itertools

from itertools import count, repeat, permutations, combinations, chain, cycle, product

counter=count(5,2)
for i in range(5):
    print(next(counter)) #this will print starts with number 5 difference with 4 of 5 times using the loop with next(counter)

colors=['orange', 'white', 'green']

cycle_colors=cycle(colors)
for i in range(10):
    print(next(cycle_colors)) #this will print colors list upto 10 times repeatedly

repeat_number=repeat(5, 4)
for i in repeat_number:
    print(i) #this will print the number 5 repeatedly 4 times

my_list_1 = [1, 2, 3]
my_list_2 = [4, 5, 6]
my_list_3 = [7, 8, 9]

new_list=list(chain(my_list_1,my_list_3,my_list_2)) #using chain, you can union all the lists into one
print(new_list)

permutation1 = [1, 2, 3]

permuation_presentation1=list(permutations(permutation1))
permuation_presentation2=list(permutations(permutation1,2)) #here you can pass the length with 2 and get the combinations

print(permuation_presentation1)

print(permuation_presentation2)

combination1=[1,2,3,4]

# combination_presentation1=list(combinations(combination1))
combination_presentation2=list(combinations(combination1,3)) #length 3 must be define as an argument in combinations

# print(combination_presentation1)

print(combination_presentation2)

#using product, you can give n no of lists as arguments and output will be in Tuple

product_list=list(product(my_list_1,my_list_2,my_list_3))
print("Product List:",product_list)

list_1 = [1, 2]
list_2 = ['a', 'b', 'c']

product_list_output=list(product(list_1,list_2))
print("Product List Output:",product_list_output)