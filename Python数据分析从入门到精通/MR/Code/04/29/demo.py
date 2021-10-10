import pandas as pd

df=pd.read_excel('grade.xls')      #导入Excel文件
df = df.set_index(['班级','序号']) #设置2级索引“班级”和“序号”
df = df.stack()
print(df)
