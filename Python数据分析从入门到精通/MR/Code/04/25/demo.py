import pandas as pd

data = [110,105,99,120,115]
index=[1,2,3,4,5]
df = pd.DataFrame(data=data,index=index,columns=['英语'])

df['升降']=df['英语']-df['英语'].shift()
print(df)
