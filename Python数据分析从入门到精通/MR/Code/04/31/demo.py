import pandas as pd

df=pd.read_excel('grade.xls',sheet_name='英语3')      #导入Excel文件
df1=df.pivot(index='序号',columns='班级',values='得分')