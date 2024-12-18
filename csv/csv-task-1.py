import csv
import os


cwd=os.getcwd()
filename="newfile.txt"
filepath=os.path.join(cwd, filename)

with open(filepath, 'r') as textfile:
    data=textfile.readlines()
# print(data)

with open('data.csv', 'w',newline='') as csvfile: #creating a new csv file and write that data into csv format
    writer=csv.writer(csvfile)
    for line in data:
        split_lines=line.strip().split()
        writer.writerow(split_lines)



