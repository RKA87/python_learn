from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
url="https://www.youtube.com/"
open_url=urlopen(url)
response=BeautifulSoup(open_url,features="html.parser")

import requests
import json

url="https://jsonplaceholder.typicode.com/posts/1"
status_code_response=requests.get(url)
print(status_code_response)

# Response in JSON format of output

json_response=status_code_response.json()
print(json_response)

# pass the data using POST, it is nothing but create the request
url1= "https://jsonplaceholder.typicode.com/posts"
data = {
    "userID": 1,
    "title": "Making a POST request",
    "body": "This is the data we created."
}
try:
    post_response=requests.post(url1,data)
    print("Response=",post_response.json())
except Exception as E:
    print("Error:",'\n',E)

from requests.auth import HTTPBasicAuth

request_url="https://github.com/"
username="rakeshkumar.akuluru@gmail.com"
pwd="Akuluru"

url_response=requests.get(url=request_url,auth=HTTPBasicAuth(username,pwd)) #this is how you can pass the username and password using HTTPBasicAuth(username,pwd)
print(url_response.status_code) #it will display just code only

# If the API call do not get as expected output, regardless the request fails
url="https://jsonplaceholder.typicode.com/postz"
res=requests.get(url)
# print(res) #it will print only response as 404
# print(res.raise_for_status()) # this will print exception error message abouut 404, what exactly it is about

try:
    res=requests.get(url)
    res.raise_for_status()
except requests.exceptions.HTTPError as Error:
    print(Error)

res=requests.get(url)
# requests.TooManyRedirects
# requests.ConnectionError
# requests.Timeout
# requests.ConnectTimeout
# requests.Response
# requests.Session


# Use Cases
test_url="https://httpbin.org/post"
r=requests.post(url=test_url,data ={'key':'value'})
print(r) #response status-code

print(r.json())


