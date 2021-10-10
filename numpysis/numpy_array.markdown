# Numpy_array

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
np.logspace(0,63,30)
```

3. 生成随机数组