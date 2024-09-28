# Files Upload using requests
from csv import reader

file_path="C:/Temp/test_file.txt"

with open(file_path) as file:
   r=reader(file)
   r=tuple(r)
#    print(r)

f=open(file_path,'r')
# print(f.read())

import requests

# url='https://httpbin.org/post'
# f=open(file_path,'r')
# response=requests.post(url,f)
# print(response.text)

def file_upload(filepath):
   f=open(filepath,'r')
   return (f)

def post_request(url,file):
    x=file_upload(file)
    response=requests.post(url,x)
    return(response)

url="https://httpbin.org/post"
file="C:/Temp/test_file.txt"

r=post_request(url,file)
print(r.text)


'''
Using URLOPEN function

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

url="https://api.github.com"
res1=urlopen(url)
print(res1)
text_parsing=BeautifulSoup(res1,"html.parser")
print(text_parsing)


'''
Using requests module
'''
import requests

res2=requests.get(url)

print("Response:",res2,'\n')

print("Response.StatusCode:",res2.status_code,'\n')

print("Response.Text:",res2.text,'\n')

print("Response.Json:",res2.json(),'\n')

