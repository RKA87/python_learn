# import datetime
# t=(1987,9,25)
# dob=datetime.datetime(t[0],t[1],t[2])
# print(dob.year)

# current=datetime.datetime.now()
# print(current)
# print(current.year)

# final=(current.year-dob.year)
# print(final)


# import random

# range_num=random.randrange(111111,222222)
# print(range_num)

# test_dictionary={"Rakesh":{"112323232432":"0"}}
# print(test_dictionary["Rakesh"].keys())


# import requests

# url="https://youtube.com/"

# res=requests.get(url)
# print(res)

# # print(res.status_code)
# # print(res.headers)
# # print(res.cookies)
# # print(res.text)
# # print(res.content)

# url1="https://httpbin.org/get"
# payload = {'key1': 'value1', 'key2': 'value2'}

# res3=requests.get(url1,payload)
# print(res3)
# print(res3.url)
# print(res3.encoding)

#ssl error

# try:
#     resp1=requests.get('https://requestb.in')
#     print(resp1)
# except Exception as E:
#     print("Error Exception:",E)

from urllib.request import urlopen
from urllib.error import HTTPError
import ssl


try:
    url="https://requestb.in"
    ssl_context=ssl._create_unverified_context()
    resp1=urlopen(url,context=ssl_context)
    print(resp1)
except HTTPError as E:
    print("Error Message:",E)
except Exception as E1:
    print("Error Message:",E1)


try:
    import requests
    url="https://requestb.in"
    resp1=requests.get(url,verify=False)
    print(resp1)
except Exception as E1:
    print("Error Message:",E1)
