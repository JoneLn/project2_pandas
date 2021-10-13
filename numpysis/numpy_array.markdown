# NumPy数组

## 目录

1. 概述
2. 数组计算
    2.1. 数组概念
    2.2. 创建数组
        (1) 简单创建数组
        (2) 从数值范围创建数组
        (3) 生成随机数组
        (4) 从已有的数组中创建数组
    2.3. 数组的基本操作
        (1) 数据类型
        (2) 数组运算
        (3) 数组的索引和切片
        (4) 数组重塑
        (5) 数组的增，删，改，查

## 概述

Numpy 以数组的形式对数据进行操作。

## 数组计算

### 数组概念
* 一维数组对应python列表；

* 二维数组本质是以数组作为数组元素的数组。二维数组包括行和列，类似于表格形状，又称为矩阵；

* 三维数组是指维数为3的数组结构，也称为矩阵列表。

* 轴的概念。轴是Numpy中的axis，指定某个axis，就是沿着这个axis做相关操作，其中二维数组中axis=0表示沿着纵轴操作，axis=1表示沿着横轴操作，但是由于一维数组的特殊性，在一维数组中axis=0表示沿着横轴操作（多做就懂了）


### 创建数组

1. 简单创建数组numpy.array()

```python
n1 = numpy.array([1,2,3])
n2 = numpy.array([[1,2,3],[1,2,3]])
n3 = numpy.array(n1, copy=True)
```

2. 从数值范围创建数组

```python
# 等差数列
np.arange(start, stop, step, dtype=None)
n4 = np.arange(1,12,3)

# 等差数列
np.linspace(start, stop, step)
n5 = np.linspace(1,12,3)

# 等比数列
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
"""
start 序列的起始值
stop: 序列的终止值
num： 要生成的样本的数量
endpoint： 是否包含stop终止值
base： 对数Log的底数
"""
n6 = np.logspace(0,63,30)
```

3. 生成随机数组

```python
# 随机0~1的数组 
np.random.rand(d0, d1, d2)

# 随机n列一维0~1数组
np.random.rand(n)

# 随机n行，m列二维0~1数组
np.random.rand(n,m)
```

```python
# 随机正太分布数组
np.random.randn(d0, d1, d2,...,dn)

# 随机生成满足正太分布的n列一维数组
np.random.randn(n)

# 随机生成满足正太分布的n行m列二维数组
np.random.randn(n,m)

```

```python
# 一定范围内的随机数组：randint()函数

np.random.randint(low_value, high_value, size=‘维度’)

# 一定范围内的n列一维数组
np.random.randint(l,h,10)

# 一定范围内的n行m列二维数组
np.random.randint(l,h,size=(n,m))

```

4. 从已有的数组中 创建数组

```python
np.asarray(a, dtype=None, order=None)

n7 = np.asarrey([1,2,3])
n8 = np.asarray((1,2,3))
n9 = np.asarray([(1,1),(2,3)])
n10 = np.asarray(([1,2],[3,4]))
```

### 数组的基本操作

1. 数据类型

|  数据类型   |         描述          |
| :---------: | :-------------------: |
|    bool_    |        布尔值         |
|    int_     |      整数，int32      |
|    intp     | 用于索引的整数，int64 |
|    int32    |       32位整数        |
|    int64    |       64位整数        |
|   uint32    |    32为无符号整数     |
|   uint64    |    64位无符号整数     |
|    float    |        浮点数         |
|   float16   |      16位浮点数       |
|   float32   |      32位浮点数       |
| datatime64  |     日期时间类型      |
| timedelta64 |  两个时间之间的间隔   |

2. 数组运算

下面的运算主要基于一维数组，且参与运算的两个数组元素位置必须一一对应。

```python
n1 = asarray([1,2,3])
n2 = asarray([4,5,6])

# 加减乘除幂运算，一一对应依次运算
n3 = n1+n2
n4 = n1-n2
n5 = n1*n2
n6 = n1/n2
n7 = n1**n2

# 数组与单独的数的运算
n8 = n1*10
n9 = n1/10
n10 = n1+10
n11= n1-10
```

3. 数组的索引和切片

数组的索引和切片，在基础课上也讲过，所以，这一课还是很好理解。

索引就是用来标记数组中对应元素的唯一数字，从0开始。

数组的切片可以理解为对数组的切割，按照等分或不等分将一个数组切割为多个片段。

```python
n1 = np.array([1,2,3])
n2 = np.array([[1,2,3],[4,5,6]])

# 索引
print(n1[0])
print(n2[1][1])
# 切片
print(n1[:1])
print(n2[1:,:1])

```

4. 数组重塑

```python
# 一维数组重塑为二维数组:reshape(n,m)
n = np.arange(0,11,1)
n1 = n.reshape(3,4)

# 数组转置
n = array([[1,2,3],[4,5,6]])
print(n.T)
```

5. 数组的增，删，改，查

（1）增加数据
```python
n1 = array([[1,2],[3,4],[5,6]]) # 三行两列
n2 = array([[10,11],[12,13],[14,15]]) # 三行两列

# 水平方向增加数据
n3 = np.hstack(n1,n2) # 三行四列

# 垂直方向增加数据
n4 = np.vstack(n1,n2) # 六行两列

```

（2）删除数据

```python
n1 = np.array([[1,2],[3,4],[5,6]])

# 删除第一行所有数据
n2 = np.delete(n1, 0, axis=1)

# 删除第二列所有数据
n3 = np.delete(n1, 1, axis=0)
```

（3）修改数组

通过索引修改数组中的某个值

```python
n1 = np.arange(1,12,1) # 一维数组
n2 = np.linspace(1,12,1,endpoint=True).reshape(3,4) # 二维数组

# 修改n1数组第7个数的值为11
n1[6] = 11

# 修改n2数组第2行3列的数值为10
n2[1][3] = 10

```

（4）查询数组

查询数组中满足条件的值

```python
n1 = np.arange(1,12,1) 

# 检索出满足条件的值
print(np.where(n1>5))

# 检索满足条件的值，满足条件后输出某一个值，不满足条件输出其他值
print(np.where(n1>5, 'T', 0))
```