import pandas as pd
excelFile = 'mrbook.xlsx'
df = pd.DataFrame(pd.read_excel(excelFile))

#按“销量”列降序排序
df=df.sort_values(by='销量',ascending=False)

#平均排名
df['平均排名']=df['销量'].rank(ascending=False)
df1=df[['图书名称','销量','平均排名']]

#最小值排名
df['最小值排名']=df['销量'].rank(method="min",ascending=False)
df_min=df[['图书名称','销量','最小值排名']]

#最大值排名
df['最大值排名']=df['销量'].rank(method="max",ascending=False)
df_max=df[['图书名称','销量','最大值排名']]
