import pandas as pd
excelFile = 'books.xls'
dfrow = pd.DataFrame(pd.read_excel(excelFile))

#按照索引值为0的行，即第一行的值升序排序
df=dfrow.sort_values(by=0,ascending=True,axis=1)




