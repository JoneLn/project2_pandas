import pandas as pd
df=pd.read_excel('1月.xlsx')
df1=df.head()

#设置“买家会员名”为行索引
df=df.set_index(['买家会员名'])
df2=df.head()
