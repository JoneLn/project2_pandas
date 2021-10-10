import pandas as pd
data = [[110,105,99],[105,88,115],[109,120,130]]
index = [1,2,3]
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=index, columns=columns)
#df['总成绩']=df.sum(axis=1,skipna=1)


