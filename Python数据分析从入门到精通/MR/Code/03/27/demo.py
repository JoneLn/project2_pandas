import pandas as pd
data = [[110,105,99],[105,88,115],[109,120,130],[112,115,140]]
name = ['明日','七月流火','高袁圆','二月二']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=name, columns=columns)

#增加数据,使用loc方法
df.loc[:,'物理'] = [88,79,60,50]   #在最后插入“物理”一列，其值为等号右边数据
