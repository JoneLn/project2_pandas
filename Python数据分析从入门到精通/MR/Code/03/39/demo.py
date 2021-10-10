import pandas as pd
df=pd.read_excel('TB2018.xls')
df['宝贝总数量'] = df['宝贝总数量'].fillna(0)
