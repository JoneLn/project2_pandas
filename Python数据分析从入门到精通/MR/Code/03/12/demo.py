import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_excel('1月.xlsx')
df1=df.head() #输出前5条数据
