import pandas as pd
excelFile = 'mrbook.xlsx'
df = pd.DataFrame(pd.read_excel(excelFile))

df1=df.groupby(["类别"])["销量"].sum().reset_index()
df2=df1.sort_values(by='销量',ascending=False)





