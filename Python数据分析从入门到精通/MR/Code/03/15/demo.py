import pandas as pd
df1=pd.read_excel('1月.xlsx',usecols=[0])                  #通过指定列索引号导入第1列
df1=df1.head()
df2 = pd.read_excel('1月.xlsx', usecols=[0, 3])            #通过指定列索引号导入第1列、第4列
df2=df2.head()
df3=pd.read_excel('1月.xlsx',usecols=['买家会员名','宝贝标题'])   #通过指定列名导入指定列
df3=df3.head()

