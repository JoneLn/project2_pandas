import numpy as np          #导入numpy模块
n1 = np.array([1,2,3])      #创建数组
n2 = np.array(n1,copy=True) #复制数组
n2[0]=3                     #修改数组中的第一个元素为3
n2[2]=1                     #修改数组中的第三个元素为1
print(n1)
print(n2)
