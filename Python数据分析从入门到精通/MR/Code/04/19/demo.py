import pandas as pd  #导入pandas模块
df=pd.read_csv('JD.csv',encoding='gbk')

#抽取数据
df2=df[['一级分类','二级分类','7天点击量','订单预定']]
for (key1,key2),group in df2.groupby(['一级分类','二级分类']):
        print(key1,key2)
        print(group)
