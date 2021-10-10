import pandas as pd
excelFile = 'mrbook.xlsx'
df = pd.DataFrame(pd.read_excel(excelFile))

#按“销量”列降序排序
df=df.sort_values(by='销量',ascending=False)
# 顺序排名
df['顺序排名'] = df['销量'].rank(method="first", ascending=False)
df1=df[['图书名称','销量','顺序排名']]


