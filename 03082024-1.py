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
while i<=5:
    os.makedirs(folder_path+name)
    i+=1

'''
Task 4:
You have a folder with various images. 
Write a python program to display the image indicated by the user input. Use pil package.

'''









