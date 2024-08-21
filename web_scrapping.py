import re
print(re.findall("ab*c", "abcd"))

print(re.findall("ab*c", "acc"))

print(re.findall("ab*c", "abcac"))

print(re.findall("ab*c", "abdc"))

'''
Important in Regular Expression, that you can find any words between two characters using ".*"

The pattern .* inside a regular expression stands for any character repeated any number of times. 
For instance, you can use "a.*c" to find every substring that starts with "a" and ends with "c", regardless of which letter—or letters—are in between:
'''
print (re.findall("a.*c", "abc"))

print (re.findall("a*.c","abbc"))

print (re.findall("a.*c", "ac"))

print (re.findall("a.*c", "acc"))

'''
WebScrapping
'''

from urllib.request import urlopen

url="https://seamoss.com/"

'''
urlopen is nothing but receiving page response
'''
page_response=urlopen(url)
print(page_response)

'''
After page response, need to read page
'''
page_read=page_response.read().decode("utf-8")
# print(page_read)

'''
Data recieved in HTML Text which is string format. 
Here we need to use string functions to aggregate the data based on our requirements
'''
# print(page_read.find("<title>"))
# print(page_read.find("</title>"))

# print(page_read[190:256])

match_result1=re.search("Seamoss Website",page_read)

match_result2=re.findall("<title>.*</title>",page_read)
print(match_result2)


'''
using .find() method we don't get accurate results, we will use regular expression to get the title data exactly

import re --> Methods to use .findall(), .search() 
'''

'''
Now get the date using another profile url 
http://olympus.realpython.org/profiles/dionysus
'''
import re
from urllib.request import urlopen

url="http://olympus.realpython.org/profiles/dionysus"
url_response=urlopen(url)

page_read=url_response.read().decode("utf-8") #page_read has HTML text data which includes <title> </title>
# print(page_read)

'''
Here
. - Any Character

* - Zero or More Occurences (It works based on before element)

? - Zero or One Occurence
'''
pattern="<title.*?>.*?</title.*?>"
title_result=re.search(pattern,page_read,re.IGNORECASE)
title=title_result.group() #from the search result it will give span record which is index using group() will give results
title=re.sub("<.*?>", "", title) #from the results generate in above text we will get exact title info using sub method
print(title)

# One more case scenario 
'''
Get the output of Name & Favorite Color
'''

from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"

url_response=urlopen(url)
page_read=url_response.read().decode("utf-8")
print(page_read)

pattern1="<h2>.*?</h2>"
results1=re.search(pattern1,page_read)
name1=results1.group()
name1=re.sub(r"<.*?>","",name1)
print(name1)

print(re.findall("Favorite.*",page_read)[1])

'''
Task 

Achieve below output using below url
http://olympus.realpython.org/profiles/aphrodite
http://olympus.realpython.org/profiles/poseidon
http://olympus.realpython.org/profiles/dionysus
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen

import re

url="http://olympus.realpython.org"
response_url=urlopen(url + "/profiles")
page_read=response_url.read().decode("utf-8")
soup_read=BeautifulSoup(page_read,fatures="html.parser")
# print(soup_read)

href_tags=soup_read.find_all("a")
print(href_tags)

results=[url+tag.get('href') for tag in href_tags]
print(results)

'''
Using MechanicalSoup
'''

# You can use urlopen with re for finding data but using Beautifulsoup it will be ease to fetch results
url="http://olympus.realpython.org/login"
page_res=urlopen(url)
# print(page_res)
page_read=page_res.read().decode("utf-8")
# print(page_read)
soup=BeautifulSoup(page_read,features="html.parser")
# print(soup)
pattern="login"
z=re.findall(pattern,page_read)
# print(z)

x=(soup.select("form"))
y=(soup.find_all("form"))

# Now Using of Mechanicalsoup
import mechanicalsoup

# Response of URL
browser=mechanicalsoup.Browser()
url="http://olympus.realpython.org/login"
page_response=browser.get(url)
print(page_response) #it gives the response status code of URL
page_in_html=page_response.soup #this prints the HTML data of webpage

form=page_in_html.select("form")[0] #it prints the form data from the html webpage in a list format. In list which has single element only so calling that element using [0]
print(form)

form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page=browser.submit(form,page_response.url)


# Dice webpage program

browser=mechanicalsoup.Browser()
url="http://olympus.realpython.org/dice"

page_response=browser.get(url)

html_page=page_response.soup
result_tag=(html_page.select("#result")[0])
print(result_tag.text)
