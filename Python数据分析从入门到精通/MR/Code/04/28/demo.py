import pandas as pd

df = pd.DataFrame({'a':[1,2,3,4,5], 'b':[(1,2), (3,4),(5,6),(7,8),(9,10)]})
print(df)

# apply函数分割元组
df[['b1', 'b2']] = df['b'].apply(pd.Series)
print(df)

#或者join方法结合apply函数分割元组
#df= df.join(df['b'].apply(pd.Series))
#print(df)
