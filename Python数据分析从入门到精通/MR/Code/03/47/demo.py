import pandas as pd
excelFile = 'mrbook.xlsx'
df = pd.DataFrame(pd.read_excel(excelFile))
#按“图书名称”和“销量”列降序排序
df1=df.sort_values(by=['图书名称','销量'])




