import pandas as pd
import numpy as np
data = [[110,120,110],[130,130,130],[130,120,130]]
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data,columns=columns)

print(df.std())
