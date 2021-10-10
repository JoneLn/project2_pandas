import pandas as pd

df=pd.read_excel('time.xls')
df1 = df.set_index('订单付款时间') #设置“订单付款时间”为索引

print(df1.resample('W').sum().head())
print(df1.resample('W',closed='left').sum())
#print(df1.resample('W',closed='right').sum())

