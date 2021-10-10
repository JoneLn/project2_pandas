import pandas as pd
excelFile = 'mrbook.xlsx'
df = pd.DataFrame(pd.read_excel(excelFile))
#按“销量”列降序排序
df=df.sort_values(by='销量',ascending=False)





