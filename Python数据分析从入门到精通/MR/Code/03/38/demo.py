import pandas as pd
df=pd.read_excel('TB2018.xls')
print(df.isnull())
print(df.notnull())

#删除缺失值
#df1=df.dropna()

#获取宝贝总数量不为空的数据
#df2=df[df['宝贝总数量'].notnull()]