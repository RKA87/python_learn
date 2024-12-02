# file_path="C:/Python/Python_Scripts/python_learn/os_directory/requirements.txt"

# with open(file_path,'r') as file:
#     content=file.readlines()
#     print(content)

import os
cwd=os.getcwd()
file_name=input("Enter the filename:")

file_path=os.path.join(cwd,file_name)
print(cwd+file_name)