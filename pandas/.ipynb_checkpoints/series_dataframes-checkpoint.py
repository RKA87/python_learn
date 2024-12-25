import pandas as pd
import numpy as np

#converting the multiple series into dataframe
series1=pd.Series(["Spark","Python", "Java", ".Net"],name="Courses") #when i keep the index instead of name it gives me error
series2=pd.Series([2000,3000, 5000, 7000],name='fees')
df1=pd.concat([series1,series2],axis=1)

print(df1)
print('\n')
