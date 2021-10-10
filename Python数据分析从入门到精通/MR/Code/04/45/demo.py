import pandas as pd

df = pd.DataFrame({'year': [2018, 2019,2020],
                   'month': [1, 3,2],
                   'day': [4, 5,14],
                   'hour':[13,8,2],
                   'minute':[23,12,14],
                   'second':[2,4,0]})
df['组合后的日期']=pd.to_datetime(df)
print(df)

