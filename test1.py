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


list1=[20,-10,100,-70,-60,-50,-40]
marks=[]
for element in list1:
    x=str(element)
    if x[0].startswith("-"):
        x=x[1:]
        x=int(x)
    else:
        x=int(x)
    marks.append(x)
print("MarksList:",marks)

class Student:
    
    marks_list=[]

    while len(marks_list)<6:
        mark=int(input("Enter Subject Marks:"))
        marks_list.append(mark)
        
    def __init__(self,id:int):
        self.id=id
            
    def f_marks_list(self):
        _final_mark_list=[]
        for element in Student.marks_list:
            x=str(element)
            if x[0].startswith("-"):
                x=x[1:]
                x=int(x)
            else:
                x=int(x)
            _final_mark_list.append(x)
        return _final_mark_list
         
    def marks_sum(self):
        return sum(self.f_marks_list())
    
    def avg(self):
        avg=self.marks_sum()/len(self.f_marks_list())
        return avg
    
    def high_mark(self):
        highest_mark=max(self.f_marks_list())
        return highest_mark
    
obj1=Student(22)
print("Student ID:",obj1.id)
obj1.marks_list
m_list=obj1.f_marks_list()
print("Final Mark List:",m_list)
total_marks=obj1.marks_sum()
print("Total Sum of Marks:",total_marks)
average=obj1.avg()
print("Average Marks:",average)
highest_mark=obj1.high_mark()
print("Highest Marks:",highest_mark)