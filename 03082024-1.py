# OS Module Tasks
'''
Task 1:
Write a program to list all the files in the current directory. 
Indicate if the file is a directory or not
'''
import os

def list_files_dir(file_path):

    list_files=os.listdir(file_path)

    file_list=[]
    dir_list=[]
    none_category=[]
    for each_element in list_files:
        if os.path.isfile(file_path+each_element):
            file_list.append(each_element)
        elif os.path.isdir(file_path+each_element):
            dir_list.append(each_element)
        else:
            none_category.append(each_element)
    return (file_list,dir_list)    

path="C:/Temp/"
file_list,dir_list=list_files_dir(path)
print("File List:",file_list,'\n')
print("Directory List:",dir_list,'\n')

'''
Task 2
Write a program to list the attributes of a file (size, access, date create, type etc)
'''
import time
file_path="C:/Temp/"
list_files=os.listdir(file_path)

dictionary_output={}
for each in list_files:
    file_size_bytes=os.path.getsize(file_path+each)
    file_size_kb = file_size_bytes / 1024
    file_size_mb = file_size_kb / 1024
    dictionary_output[each] = [(file_size_mb),time.ctime(os.path.getatime(file_path+each)),time.ctime(os.path.getctime(file_path+each))]

print("Size of Folders and Files in the Directory:"'\n',dictionary_output)

'''
Task 3:
Using the os module, create a number of directories (folders) indicated by the user input. 
The directories should be nested. Limit the number to 5

'''
number=1
folder_path="C:/Temp/"
name="test"

i=1
x=folder_path+name
while i<=5:
    os.makedirs(x)
    i+=1
    x=x+name

# case 2
path="c:/Temp/"
directory="test"

current_path=path

for i in range(1,6):
    current_path=os.path.join(current_path,directory)
    os.makedirs(current_path)

'''
Task 4:
You have a folder with various images. 
Write a python program to display the image indicated by the user input. Use pil package.

'''
from PIL import Image
import os

def display_image(file_path,image_no_input):
    list_images=os.listdir(file_path)

    # filtering JPEG images only
    pics_list=list(filter(lambda image:image.endswith(".jpg"), list_images))
    image_indicate_directory={}

    for i in range(len(pics_list)):
        image_indicate_directory[i]=pics_list[i]

    try:
        # Display Image (image_indicate_directory)
        display_image=image_indicate_directory[image_no_input]
        open_file=Image.open(file_path+display_image)
        return (open_file.show())
    # except (KeyError,AttributeError,NameError,TypeError,SyntaxError) as E:
    #     return ("Please Enter Input Range is from 0 to 3 only")
    except Exception as ErrorInfo:
        return ("Error Info:",ErrorInfo, "Enter Input Range is from 0 to 3 only")

file_path="C:/Temp/"
image_no_input=1
result=display_image(file_path,image_no_input)
print(result)

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