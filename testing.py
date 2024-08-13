# import os
# file_path="C:/Temp/"
# name="test"
# os.makedirs(file_path+name)

from PIL import Image

import os
pics_folder_path="C:/Users/rakes/Downloads/pics/"
list_images=os.listdir(pics_folder_path)

image_indicate_directory={}

for i in range(len(list_images)):
    image_indicate_directory[i]=list_images[i]

# print(image_indicate_directory)

user_input=int(input("Enter a number to display the image as per directory:"))

display_image=image_indicate_directory[user_input]

open_file=Image.open(pics_folder_path+display_image)
open_file.show()