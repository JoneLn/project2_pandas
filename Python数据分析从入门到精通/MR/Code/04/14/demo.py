import pandas as pd

data = [['零基础学Python','1月',49768889],['零基础学Python','2月',11777775],['零基础学Python','3月',13799990]]
columns = ['图书','月份','码洋']
df = pd.DataFrame(data=data, columns=columns)
df['码洋']=df['码洋'].apply(lambda x:format(int(x),','))
print(df)