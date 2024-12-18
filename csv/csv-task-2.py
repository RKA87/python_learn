import csv, os

header=['Team','Games','Wins','Losses','Draws','Goals For','Goals Against']
data=['Arsenal',38,26,9,3,79,36]

cwd=os.getcwd()
filename="data1.csv"
filepath=os.path.join(cwd, filename)

with open(filepath,'w',newline='') 