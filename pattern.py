# case 1 
# 1
# 22
# 333
# 4444
# 55555

for row in range(1,6):
    for col in range(row):
        print(row, end=" ")
    print(" ")

# case 2
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for row in range(1,7):
    for col in range(1,row):
        print(col, end=" ")
    print(" ")
print('\n')

# case 3
# inverted pyramind pattern
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5
b=0
for row in range(6,0,-1):
    b = b+1
    for col in range(row):
        print(b, end=" ")
    print(" ")
print('\n')
# case 4
# inverted half pyramind pattern
# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1

for row in range(6,0,-1):
    for col in range(0,row):
        print(col, end=" ")
    print(" ")
print("\n")

# case 5
# inverted half pyramind pattern
# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9
b=0
for row in range(1,6):
    b = b+1
    for col in range(row):
        print(b, end = " ")
    b+=1
    print(" ")
print("\n")
# case 6
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

for row in range(6,0,-1):
    for col in range((row-1),0,-1):
        print(col, end=" ")
    print(" ")
print("\n")
# case 7
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *
x="*"
for row in range(6,0,-1):
    for col in range(row):
        if col < row:
            print(" ", end=" ")
        else:
            print(x, end=" ")
    print(" ")