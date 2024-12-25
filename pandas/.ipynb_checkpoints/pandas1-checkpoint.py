import pandas as pd
import numpy as np

data = np.array(["python","php","java"])
series=pd.Series(data)
print(series)


data1 = {'Courses' :"pandas", 'Fees' : 20000, 'Duration' : "30days"}
s2=pd.Series(data1)
print('\n')
print(s2)

#the same series s2 data can be print along with index format
print('\n')
s2=pd.Series(data1.keys(), index=['r1','r2', 'r3'])
print(s2)

data2=np.array(["1", "2", "rakesh", "raj", "23548.534"])
s3=pd.Series(data2, index=['row1','row2', 'row3', 'row4', 'row5'])
print('\n')
print(s3)

# Using Data Dictionary above specifiying the index's now
# When using the dictionary it will points the keys for indexing
# you will get result NaN, because your indexing values does not match with keys in dictionary
data3 = {'Courses' :"pandas", 'Fees' : 20000, 'Duration' : "30days"}
s4=pd.Series(data3, index=['Courses', 'Course_Fee', 'Course_Duration'])
print('\n')
print("S4 Series:",s4)


data4=["ram", "suji", "rakesh","rani"]
s5=pd.Series(data4)
print('\n')
print(s5)

s = pd.Series()
print(s)