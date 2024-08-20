'''
Author: shgopher shgopher@gmail.com
Date: 2024-08-18 11:42:15
LastEditors: shgopher shgopher@gmail.com
LastEditTime: 2024-08-20 23:51:36
FilePath: /PythonFamily/learn-python-by-examples.py
Description: 

Copyright (c) 2024 by shgopher, All Rights Reserved. 
'''
# learn-python-by-examples.py
# 使用例子学习 Python
## python 版本 Python3

# 开始

# 1. hello world
print("hello world \n")

# 2. 数据类型
a = 1 # 整数
b = "hello world" # 字符串
c = 'h' # 字符
d = True # 布尔类型
e = ['1',2.0,3] # 列表 :更灵活的切片
f= (1,'2',1) # 元组
g = {'1',1,1.0} # set ：只有key的map
h = {'name':'shgopher','age':18} # map

print(a,b,c,d,e,f,g,h,'\n')

# 3. 类型转换
## 隐性转化
j = 1
i = 1.0
value = j + i # 2.0 ,j 阴性转化为1.0 了
print(value)
## 显性转化
### int 转换
num_str = "8"
num_int = int(num_str)
print("将字符串 '10' 转换为整数：", num_int)

### float 转换
num = 5
num_float = float(num)
print("将整数 5 转换为浮点数：", num_float)

### complex 转换
real = 2
imag = 3
num_complex = complex(real, imag)
print("将 2 和 3 转换为复数：", num_complex)

### str 转换
num = 100
str_num = str(num)
print("将整数 100 转换为字符串：", str_num)

### bytes 转换
text = "Hello"
bytes_text = bytes(text, encoding='utf-8')
print("将字符串 'Hello' 转换为字节：", bytes_text)

### list 转换
tuple_data = (1, 2, 3)
list_data = list(tuple_data)
print("将元组 (1, 2, 3) 转换为列表：", list_data)

### tuple 转换
list_data = [4, 5, 6]
tuple_data = tuple(list_data)
print("将列表 [4, 5, 6] 转换为元组：", tuple_data)

### set 转换
list_data = [7, 7, 8, 8, 9]
set_data = set(list_data)
print("将列表 [7, 7, 8, 8, 9] 转换为集合：", set_data)

### dict 转换
### 此处示例将两个列表组合成字典
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_data = dict(zip(keys, values)) # zip 是将list 组合成元组
print("将两个列表组合成字典：", dict_data)

### chr 转换
num = 65
char = chr(num)
print("将 65 转换为字符：", char)

### ord 转换
char = 'A'
num = ord(char)
print("将字符 'A' 转换为编码：", num)

### bin 转换
num = 10
bin_num = bin(num)
print("将整数 10 转换为二进制：", bin_num)

### oct 转换
num = 10
oct_num = oct(num)
print("将整数 10 转换为八进制：", oct_num)

### hex 转换
num = 10
hex_num = hex(num)
print("将整数 10 转换为十六进制：", hex_num)

### eval 转换
expr = "2 + 3"
result = eval(expr)
print("对表达式 '2 + 3' 求值：", result)

### repr 转换
obj = [1, 2, 3]
repr_str = repr(obj)
print("将列表 [1, 2, 3] 转换为字符串表示：", repr_str)

### type 转换
num = 5
print("5 的数据类型：", type(num))

# 4. 运算符
## 4.1 算术运算符
a = 10
b = 5
print(a + b,a-b,a*b,a/b,a%b,a**b,a//b)

