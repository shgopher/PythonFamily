'''
Author: shgopher shgopher@gmail.com
Date: 2024-08-18 11:42:15
LastEditors: shgopher shgopher@gmail.com
LastEditTime: 2024-08-29 11:56:38
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
## 4.2 比较运算符
print(a==b,a!=b,a>b,a<b,a>=b,a<=b)
## 4.3 赋值运算符
a = 10
a += 5
a -= 5
a *= 5
a /= 5
a %= 5
a **= 5
a //= 5

if (a:= 10)> 5:
    print(a)

## 4.4 位运算符
a = 10
b = 5
print(a & b,a | b,a ^ b,~a,a << b,a >> b)
## 4.5 逻辑运算符
a = True
b = False
print(a and b,a or b,not a)
## 4.6 成员运算符
a = [1,2,3]
print(1 in a,1 not in a)
## 4.7 身份运算符
a = [1,2,3]
b = [1,2,3]
print(a is b,a is not b)
c = [1,2,3]
d = c
print(c is d)
## 5.数字类型 number
a = 1
b = 1.0
c = 1+ 1j
print(a,b,c) 
## 6.字符串 string
a = "lixiang"
print(f"{a}是第一个来的学生")
## 7.列表 list
myList = [1,2,3,4]

for i in myList:
    print(i)

print(myList[-1])
myList.append(4)
myList.insert(0,10)
myList.pop()
myList.remove(4)
myList.sort()
print(myList)
## 8.元组 tuple
tup1 = (1,2,"3")
tup2 = (11,22,23)
for i in tup1:
    print(i)
    
tup3 = tup1 + tup2

## 9.字典 dict
dict1 = {"name":"shgopher","age":18}
for i in dict1:
    print(i)
del dict1["name"]
dict1.pop("age")
print(dict1)
## 10.集合 set
set1 = {1,2,3}
set2 = set([1,2,3])
for i in set1:
    print(i)

## 11.条件语句
a = 12
if a > 10:
    print("a 大于 10")
elif a < 10:
    print("a 小于 10")
else:
    print("a 等于 10")
b  = 10
def myage(a):
  match a :
      case 10:
          print("a 等于 10")
      case 1:
          print("a 等于 1")
      case _:
          print("a 不等于 10")

## 12.循环语句
n = 100
while n > 0:
    print(n)
    n -= 1 

a = "hello world"

for i in a:
    print(i)

## 13.推导式
### 13.1列表推导式
hiList = ["hello", "world",1,2]
hiList = [name.upper() for name in hiList if isinstance(name,str)]
print(hiList)
## 13.2字典推导式
hiDict = {"name": "hello", "age": 18}

hiDict = {key: value for key, value in hiDict.items() if key == "name"}
print(hiDict)

hiDict = ["hidd","dsd","sd","sddsd"]
hiDict = {i: len(i) for i in hiDict}
print(hiDict)
### 13.3集合推导式
hiSet = ["hidd","dsd","sd","sddsd"]
hiSet = {i for i in hiSet}
print(hiSet)
### 13.4 元组推导式
hiTuple = (i for i in range(1,10)) # 返回的是一个生成器，所以需要再处理成元组
hiTuple = tuple(hiTuple) # 从生成器处理成元组
print(hiTuple)
## 14.迭代器
iterator = iter([1,2,3])

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) ,如果迭代器已经迭代完，会报错

list = [1,2,3,4,5]
for i in iter(list):
  print(i)

li = [1,2,3,4,5]
# print(next(list)) 这是错误用法，因为 li 并没有实现迭代器，所以不能使用next()方法
for i in li: # 你会发现，不需要给定list这种内置数据迭代器，也可以使用 for in 这种range方法，但是不能使用 next()方法
  print(i)

class MyNumber :
  def __iter__(self): # 这个表示第一个数据
    self.a = 111
    return self
  def __next__(self): # 这个表示后续每次调用next，都会返回的数据 
    x = self.a
    self.a += 2
    return x
  
myclass = MyNumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
## 15.生成器
def number(n):
  while n > 0:
    yield n
    n -=1
g = number(10)
print(next(g))
print("---")
for i in g:
  print(i)
## 16.函数
def hello(name="hello"):
  if name == "hello":
    return "hello world" , 12
  return -1

print(hello("1"))

def hi(*args):
   for i in args:
     print(i)

hi("d","d","o","s")
def hello(**kwargs):
  for key, value in kwargs.items():
    print(key, value)

hello(a=1, b=2)
## 17.lambda
c = lambda x: x + 1
print(c(12))
## 18.装饰器
def hello(name):
  def inner():
    print("hello", name)
    name()
    print("hi", name)
  return inner 
@hello
def hi():
  print("---")

hi()
## 19.模块

## 20.异常处理

## 21.面向对象编程

## 22.命名空间

## 23.作用域

## 24.输入输出

## 25.file

## 26.os

## 27.并发编程


