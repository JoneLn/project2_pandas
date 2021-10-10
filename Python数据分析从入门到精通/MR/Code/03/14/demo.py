import pandas as pd
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df1=pd.read_excel('1月.xlsx',index_col=0)  #设置“买家会员名”为行索引
df1=df1.head()
df2=pd.read_excel('1月.xlsx',header=1)     #设置第1行为列索引
df2=df2.head()
print(df2)
df3=pd.read_excel('1月.xlsx',header=None)  #列索引为数字
df3=df3.head()
#通过索引快速检索数据
print(df3[0])
print(df1.loc['mrhy1'])
