import pandas as pd
import numpy as np
data = [[110,113,102,105,108],[118,98,119,85,118]]
index=['小黑','小白']
columns = ['物理1','物理2','物理3','物理4','物理5']
df = pd.DataFrame(data=data,index=index,columns=columns)
print(df.var(axis=1))

