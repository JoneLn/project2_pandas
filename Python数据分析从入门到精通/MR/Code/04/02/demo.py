import pandas as pd
data = [[110,105,99],[105,88,115],[109,120,130],[112,115]]
index = [1,2,3,4]
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=index, columns=columns)
new=df.mean()
#增加一行数据（语文、数学和英语的平均值,忽略索引）
df=df.append(new,ignore_index=True)


