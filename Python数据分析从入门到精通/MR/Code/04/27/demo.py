import pandas as pd

#导入Excel文件部分列数据（“买家会员名”和“宝贝标题”）
df = pd.read_excel('mrbooks.xls',usecols=['买家会员名','宝贝标题'])
#使用join方法和split方法分割“宝贝标题”
df = df.join(df['宝贝标题'].str.split('，', expand=True))
df1=df.head()

