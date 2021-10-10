import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('体温.xls') #导入Excel文件
#折线图
x =df['日期']                #x轴数据
y=df['体温']                 #y轴数据
plt.plot(x,y)



