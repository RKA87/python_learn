import os

def get_files_directories(path):

    # get the list of files and directories in the specified path
    get_list=os.listdir(path)

    # check if it is file or directory from the above list
    file_list=[]
    dir_list=[]
    for each in get_list:
        if os.path.isfile(path+each):
            file_list.append(each)
        else:
            os.path.isdir(path+each)
            dir_list.append(each)
    return (path, file_list, dir_list)

path="C:/Python/"
path,files_list,dir_list=get_files_directories(path)

print("Given Path:",path)
print("Files List:",files_list)
print("Directory List :",dir_list)

'''
Task 2
write a program to list attributes of a file (size,access,date create,type etc)
'''
import time

filename="C:/Temp/lib"

access_t=(os.path.getatime(filename))
create_t=(os.path.getctime(filename))
modifi_t=(os.path.getmtime(filename))

size=(os.path.getsize(filename))

print(access_t, create_t, modifi_t)

# since getatime, getctime are displayed output as string format time we can use time module to get date & year

# getctime = create time & getatime = access time & getmtime = modified time

print("Access Time:",time.ctime(access_t))
print("Create Time:",time.ctime(create_t))
print("Modify Time:",time.ctime(modifi_t))

'''
Task 3
write a program to create the directory under nested directory based on user input and limit to create 5
'''
path="c:/Temp"
directory="/test"

# case 1
i=1
x=path+directory
while i<6:
    os.makedirs(x)
    i+=1
    x=x+directory

# case 2

path="c:/Temp/"
directory="test"

current_path=path

for i in range(1,6):
    current_path=os.path.join(current_path,directory)
    os.makedirs(current_path)

'''
Task 5
Accept some input from the user and write it to a text file
'''

# case 1
text_input=input("Enter the input to save required data:")

file_path="C:/Temp/test.txt"
with open(file_path, 'w') as file:
    file.write(text_input)

# case 2 using writelines

# Open a non-existent file in write mode
fo = open("C:/Temp/new.txt", "w")
print("Name of the file: ", fo.name)

# Write a new text
seq = ["Hello", '\n', "Welcome to Tutorialspoint"]
line = fo.writelines(seq)

print("Check the file to see the reflected changes")

# Close opened file
fo.close()

'''
Task 6
read a tex file from folder and display the count of the word entered by the user in the file
'''

fo=open("c:/Temp/new.txt",'r')
file_read=fo.read()

# # I've got the output is in list after split from the text file words. In the second line when the split does it creates "Hello'\n'World" like this.
# to overcome this we can use splitlines and get the lists output with elements

output_lines=file_read.splitlines("") 
output_words=[]
for word in output_lines:
    for each_word in (word.split(" ")):
        output_words.append(each_word)

for length in output_words:
    print(f"count of '{length}' word:",len(length))