# Read the file, file not found error exception
import csv

# try:
#     with open("C:/Temp/all_games.csv",'r',encoding='utf-8') as file:
#         for each_row in file:
#             print(each_row)
# except (FileNotFoundError, UnicodeDecodeError) as E:
#     print("Error Message:",'\n',E)

try:
    file=open("c:/Temp/all_games.csv",encoding='utf-8')
    file_reader=csv.reader(file)
    all_games=list(file_reader)
    
    # for each_game in all_games:
    #     print(each_game)
except (FileNotFoundError,UnicodeDecodeError) as E:
    print("Error Message:",'\n',E)

'''
Task 2
Place the file in the correct location and read the file. 
Process the record and try to parse the user_review column and convert it to a float.  
If the ValueError occurs set the value to 0.0 and continue processing the records 
'''
# create the dictionary to store with name & user_review headers
# name_user_review_dict = {}
# try:        
#     for game in all_games[1:]: #now excluding the header row in csv sheet so all_games list is starts with 1cls
#         name=game[0]
#         if type(game[5]) == float:
#             user_review=float(game[5])
#         elif type(game[5]) == str:
#             val=0.0
#             user_review=val
#         name_user_review_dict[name]=user_review
# except Exception as Err:
#     print("ErrorInfo:",'\n',Err)

# print(name_user_review_dict)

# Extracting the Date
name=[]
platform=[]
date=[]

for game in all_games[1:]:
    name.append(game[0])
    platform.append(game[1].replace(" ", ""))
    date.append(game[2])

nested_d={}

for n,p,t in zip(name,platform,date):
    nested_d[n]={"platform":p,"date":t}

from datetime import datetime

def year_fetch_from_date(element):
    list=[]
    for element in date:
        x=datetime.strptime(element,"%d-%b-%y")
        x=x.strftime('%d-%m-%Y')
        x=x.split("-")[2]
        list.append(x)
    return list
        
cal_year=year_fetch_from_date(date)


'''
Here Nested_d - key is Name and Value is Platform & date
'''
for (title,loop_elements) in nested_d.items():
    for (platform,date) in loop_elements:
        loop_elements.update({platform:datetime.now().year})    
    nested_d.update({title:loop_elements})
print(nested_d)
# print(list(nested_d.items())[:5])
