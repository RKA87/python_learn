import time

'''
time module reqquires the string format output, this is the one consider to pass as an obj or argument in the function methods of time
string format should be "1627987508.6496193"

using time we will get output in string as seconds type

ctime=convert time
gmtime=greenwich mean time, this shows output as unix structed time output
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=6, tm_wday=3, tm_yday=1, tm_isdst=0)
asctime=Asci time

output will be in string as seconds format
'''
import datetime
print(time.gmtime(1723233164.24354)) #display as unix structured time format type

print(time.time()) #get the string format output time "1723233164.24354"

print(time.localtime(1723233164.24354)) #display as unix structed time format type

print(time.ctime(1723233164.24354)) #input object as string format one result display as "Fri Aug  9 14:52:44 2024"

s = time.strftime("%a, %d %b %Y %H:%M:%S", 
             time.localtime(1627987508.6496193))
print("Readable Format Time:",s)

#structured displayed time output can be convert into date time year type

obj1=time.gmtime(1723233164.24354)
obj2=time.localtime(1723233164.24354)

print(time.asctime(obj1))
print(time.asctime(obj2))