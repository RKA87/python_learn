'''
Following this article link example
https://www.dataquest.io/blog/python-dictionary-comprehension-tutorial/
'''

import csv
from csv import reader

'''
file_path can be load in different ways using with open() or open()

Using "with" method you will be able to load the file with read/write mode and also error will get exception and share the result automatically in python

Using "open" method only, you will be able to load the file with read/write mode but the error won't be exceptional, you must load the file and fix the errors
accordingly which it has "UnicodeDecode", "UnicodeEncode" or any different error will arise. We must fix it using the try cahce & except methods

"Defining FilePath's in numerous types

Windows_file_path = C:\Temp\all_games.csv (By default it will be look like this), you need to load the fileshare path by changing the backlash(\) to forwardlash(/) or doublelash(\\)

now
windows_file_path = C:/Temp/all_games.csv or C:\\Temp\\all_games.csv
'''

# case:1 Loading file from fileshare path - Using with method to open the file

file_path = "C:/Temp/all_games.csv"
# try: 
#     with open (file_path,'r',encoding="utf-8") as file:  #It triggers "UnicodeDecodeError"
#         # for row in file:
#         #     print(row) #It loads as a string of every row so we need to use reader function for file and row can be generate in a list of every row so this process is not useful

#         all_games=reader(file) #by defining reader to the file is must, it prints every single row as list which has elements
#         for game in all_games:
#             print(game) #Now it display as list element of each row since all_games has no of lists of each row, so you can call header using list slicing concept game[0]

# except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError, AttributeError) as Error:
#     print("Error:", Error)

# case:2 Loading file from fileshare path - Using open method only to open the file
try:
    all_games=open(file_path,encoding="utf-8")
    all_games=reader(all_games)
    all_games=list(all_games) #for parsing the csv content and manipute the data multiple times we must define it in list so that you can call the elements of row wise using for loop below
    
    # for game in all_games[1:5]: 
    #     print(game, '\n')
except (UnicodeDecodeError,NameError,UnicodeEncodeError,UnicodeError,AttributeError,TypeError,SyntaxError) as Error:
    print("Error Message:",Error)

# Note: so far we did make sure to load the data, reader data, list data, loop the data and print that data exactly in our way 

'''
Now Data Manipulation starts using the all_games.csv dataset based on the above case 1 & case 2 output

This dataset contains the following information:

Name
Platform
Release Date
Summary of the story
Meta Score
User Score

'''

# create the dictionary to store game platform based on header
platform_dict = {}

for game in all_games[1:]: #now excluding the header row in csv sheet so all_games list is starts with 1cls
    
    name=game[0]
    platform=game[1]
    platform_dict[name]=platform

# print(platform_dict)

# Now printing the first 5 itmes from ditionary using list definitive
print(list(platform_dict.items())[:5])


# Notice that each platform has a space before its name, so let's remove it. It is doable with either a for loop or dictionary comprehension.
# case 1
# using for loop
for name,platform in platform_dict.items():
    # x=platform.strip()
    # print(x)
    # platform_dict[name]=x
    platform_dict[name]=platform.strip() #strip and save the value and again make sure to save in the key.. use one line key=value.strip() this will automatically update the value for key

# case 2 
# using dictionry  comprehension
platform_dict={name:platform.strip() for name,platform in platform_dict.items()}

# print(platform_dict)
print(list(platform_dict.items())[:5]) #testing purpose to understand only

# Initialize empty lists to store column values (name, platform, date, summary, meta_score & user_score) Header from Dataset
name=[]
platform=[]
date=[]
summary=[]
meta_score=[]
user_score=[]

# Iterate over columns and append values to lists

for game in all_games[1:]:
    name.append(game[0])
    platform.append(game[1].replace(" ", "")) #it removes the space
    date.append(game[2])
    summary.append(game[3])
    meta_score.append(game[4])
    user_score.append(game[5])

# Dictionary to store dates
date_dictionary={}

# Filter the Year from Date
def year_result(date_element):
    from datetime import datetime
    x=(datetime.strptime(date_element,"%d-%b-%y"))
    x=x.strftime('%d-%m-%Y')
    return x.split("-")[2]

date_list=[year_result(date_element) for date_element in date]

for key,value in zip(name,date_list):
    date_dictionary[key]=value

# print(date_dictionary) #it is year_dict in document

# Print release year of Grand Theft Auto IV
print(f"Grand Theft Auto IV was released in {date_dictionary['Grand Theft Auto IV']}.")

# Let’s recreate the dictionary of video games released after 2014.
# In this case, name is nothing but GameName and date you can get it from date_list

after_2014={key:value for key,value in zip(name,date_list) if int(value) >2014}

print("First Five in After 2014:",list(after_2014)[:5])

# Let’s recreate the dictionary of video games released from 2014 to 2018
# In this case, name is nothing but GameName and date you can get it from date_list

from_2014_2018={key:value for key,value in zip(name,date_list) if int(value) >=2014 and int(value) <= 2018}

print("Video Games Released from 2014 to 2018:"'\n',list(from_2014_2018.items())[:5])

# Let’s recreate the dictionary of video games meta score below 24 or above 97
# In this case, name is nothing but GameName and MetaScore you can get it from meta_score

meta_25_97={key:value for key,value in zip(name,meta_score) if int(value) <25 or int(value) >97}

print("MetaScore below 25 and above 97:",'\n',meta_25_97)

# Creating Nested Dictionary Comprehension

def formatted_date(element):
    from datetime import datetime
    x=datetime.strptime(element, "%d-%b-%y")
    return x.strftime("%B %d, %Y")

format_data=[formatted_date(element) for element in date] #fomat_data element output: December 02, 2008

nested_d={}

# using for loops case 1
# for n,p,dt in zip(name,platform,format_data):
#     nested_d[n]={"platform":p, "Date":dt} #Here creating a dictionary "nested_d" and its values are passing dictionary

# using comprehension case 2
nested_d={n:{"platform":p,"date":dt} for n,p,dt in zip(name,platform,format_data)} #Important one to remember, storing values as dictionary type

print("Nested Dictionary:",'\n',list(nested_d.items())[:5])

# Extract release years and transform them into integers inside the nested dictionary
for (title,outer_value) in nested_d.items():
    for (inner_key,time_period) in outer_value.items():
        # try:
        #     outer_value.update({inner_key:int(time_period[-4:])})
        # except:
        #     print("Time Period:",time_period)
        if inner_key == 'date':
            outer_value.update({inner_key:int(time_period[-4:])})

nested_d.update({title:outer_value})

print("Latest Nested Dictionary:",list(nested_d.items())[:5])

# Sorting a Dictionary with Comprehension

date_dictionary_int={key:int(value) for key,value in date_dictionary.items()}

# Sorting by the year

sorted_year={key:value for key, value in sorted(date_dictionary_int.items(),key=lambda x:x[1])}

print("Sorted Year Wise:",list(sorted_year.items())[:5])

# Flattening of Dictionaries

# Word Frequency

quote = """time is too slow for those who wait too swift for those who fear too long for
those who grieve too short for those who rejoicebut for those who love, time is eternity"""

# case 1
# list_output=quote.split(" ")

# dict_output={}
# for each in list_output:
#     dict_output[each]=list_output.count(each)
# print(dict_output)

# Using comprehension
output_dict={each:quote.split().count(each) for each in quote.split()}

print(output_dict)
