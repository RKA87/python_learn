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
