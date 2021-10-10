import pandas as pd

df=pd.read_excel('TB2018.xls')
df1=df.dropna()
df2=df.dropna().reset_index(drop=True)
