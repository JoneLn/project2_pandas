import pandas as pd
data = [[110,105,99],[105,88,115],[109,120,130]]
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data,columns=columns)
print(df)

