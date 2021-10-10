import pandas as pd

df=pd.DataFrame({'原日期':['14-Feb-20', '02/14/2020', '2020.02.14', '2020/02/14','20200214']})
df['转换后的日期']=pd.to_datetime(df['原日期'])
print(df)

