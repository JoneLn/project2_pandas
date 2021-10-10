import pandas as pd
data = [[110,120,110],[130,130,130],[130,120,130]]
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data,columns=columns)
print(df.mode())           #三科成绩的众数
print(df.mode(axis=1))     #每一行的众数
print(df['数学'].mode())   #“数学”的众数
