<!--
 * @Author: shgopher shgopher@gmail.com
 * @Date: 2024-08-18 11:41:33
 * @LastEditors: shgopher shgopher@gmail.com
 * @LastEditTime: 2024-08-26 00:39:13
 * @FilePath: /PythonFamily/HelloPython.md
 * @Description: 
 * 
 * Copyright (c) 2024 by shgopher, All Rights Reserved. 
-->
# 快速入门 Python
## 基本类型

Python 中的变量没有类型，它可以被赋予任何类型的参数

所以它不能使用 a int 或者 int a 或者 a:int 这种方式去声明变量
不过变量必须被赋值，它不像 go 是自动拥有默认值的，Python 必须显的赋值。

python 没有字符，字符串是一个的就是字符，通常我们喜欢使用 ‘’ 表示字符

- 字符串

- number：int float bool (bool 是 number 的子类 0 1 表示 false true) complex

- list 就是不同类型的切片 [1,1.0,true，“1.0”]，跟元组也不一样，元组虽然是不同类型的，但是元组的元素不能修改，list 可以修改，所以你可以理解为它是不同类型的切片

- tuple 元组，可以理解为不可修改的 list a =(1,1.0，‘1.0’)

- Set 可以理解为只有 key 的 map a = {1,1.0，‘1.0’}

- 字典，或者也可以叫 map 就是一般意义的那个 key-value 的 map a = {1:1.0,1.0：‘1.0’} key 具有唯一性，set 也一样

- bytes 类型不可变的二进制序列 a = b'hello' 或者 a= bytes (‘hello’，‘utf-8’) 其实就是字符类型，默认使用 utf-8 编码通过内置函数 ord 将字符类型转化为编码中的 int 类型

## 类型转换

- 阴性类型转换
- 显性类型转换

***隐性：***

```python
a = 1.0
b = 1

c = a+b #  2.0 b 阴性转化为1.0
```
***显性：***

|函数|描述|
|:---:|:---:|
|int(x [,base])|将 x 转化为 int 类型，（例如：8不能转化为二进制，会报错）|
|float(x)|将 x 转化为 float 类型|
|complex(real [,imag])|将 real 和 imag 转化为 complex 类型|
|str(x)|将 x 转化为 str 类型|
|bytes(x [,encoding[,errors]])|将 x 转化为 bytes 类型|
|list(x)|将 x 转化为 list 类型|
|tuple(x)|将 x 转化为 tuple 类型|
|set(x)|将 x 转化为 set 类型|
|dict(x)|将 x 转化为 dict 类型|
|chr(x)|将 整数 x 转化为字符类型|
|ord(x)|将 x 转化为编码类型|
|bin(x)|将 x 转化为二进制类型|
|oct(x)|将 x 转化为八进制类型|
|hex(x)|将 x 转化为十六进制类型|
|eval(x)|将 x 转化为表达式类型|
|repr(x)|将 x 转化为字符串类型|
|type(x)|将 x 转化为类型类型|

## 运算符
### 算术运算符
- \+ 加
- \- 减
- \* 乘
- / 除
- % 取模
- ** 幂
- // 取整除 2//3 = 0； -9//2 = -5 (这个注意，往小的方向取整数，所以是-5 不是-4)
### 比较运算符
- \==
- \!=
- \>
- \<
- \>=
- \<=
### 赋值运算符
- \= 赋值
- \+=
- \-=
- \*=
- /=
- %=
- \**=
- \//= 去整
- \:= 海象运算符 (跟 go 的:= 不是一个概念)(用法：if (n := 1) > 1：)
### 位运算符
- \& 位与
- \| 位或
- \^ 位异或
- \~ 位取反
-\<< 左移
- \>> 右移
### 逻辑运算符
有一说一，Python 这种用法挺奇怪的，其它的都是 && || ！

- and
- or
- not

### 成员运算符
- in：x in y，如果 x 在 y 中，返回 True
- not in：x not in y，如果 x 不在 y 中，返回 True
### 身份运算符
Python 拥有引用类型的，所以有时候需要判断两个变量是不是引用同一个对象，这时候可以用 is 运算符

- is：x is y，如果 x 和 y 是引用的同一个对象，返回 True
- is not：x is not y，如果 x 和 y 引用的不是同一个对象，返回 True
## 数字类型 number
- int
- float
- complex
## 字符串 string
- string

字符串是引用类型，支持下标访问，不支持更改

字符串格式化 `print("这是%s" % a)`，不能使用逗号，逗号表示并列关系，所以要使用 `%`

python 使用三引号表示可以换行的字符串
```py
nowStr = """
你好

你好
"""
```

f-string

格式化字符串以 f 开头，后面跟字符串，字符串表达式使用大括号

```py
x = 1
print(f"这是{x+1}个")
```
使用 f-string 就不用判断是数字还是字符串了
## 列表 list
可以理解为拥有不同类型的切片，Python 的 list 可以拥有的操作是索引，切片，加乘检查成员
```py
list1 = [1,1.0,true,"1.0"]

list1[0] // 索引
list1[-1] // 从后面索引
list1[0:2] // 切片


```
使用 append 向后添加数据 `list1.append(1)`

使用 del 删除元素 `del list1[0]` // 删除第一个元素

比较 list，也就是比较 list 的元素是否相同
```py
import operator
if operator.eq(list1,[1,1.0,true,"1.0"]):
  print("相等")
  else:
    print("不相等")
```
### 运算符
- len() 返回 list 长度
- value = list1 + list2 // list 拼接
- value = list1 * 2 // list 重复
- in：判断 list 中是否包含某个元素
### list 内置函数
- len() 返回列表长度
- max() 返回 list 的最大值
- min() 返回 list 的最小值
- list() 将 tuppple 转化为 list
### 内置方法
- list.append(obj) 在某个 list 后面添加元素
- list.count(obj) 返回 obj 在 list 中出现的次数
- list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值 (用新列表扩展原来的列表)
- list.index() 返回指定元素在列表中的位置，如果没有该元素，则返回-1
- list.insert() 在指定位置插入元素
- list.pop() 删除指定位置的元素，并返回该元素，默认是删除最后一个元素
- list.remove(obj) 删除指定元素，删除第一个匹配的元素，如果元素不存在，则抛出异常
- list.reverse() 列表反转
- list.sort() 列表排序
- list.clear() 清空列表
- list.copy() 复制列表
## 元组 tuple
tuple 是不可改变的 list

元组跟 list 不同，它后面是小括号 tup1 = (1,1.0,true，“1.0”)

tuple 是不可变的，不能修改，所以不能使用 append，但是可以切片，所以可以用来判断是否相等

元组只有一个元素的时候要加上逗号 `tup1 = (1,)` 不然 Python 会认为后面是一个 number 类型

当索引元组的时候，跟 list 相同也是 tup1[0] 即可，也是中括号

元组无法更改，但是两个元组可以加在一起生成一个新的元组 `tup3 = tup1 + tup2`

元组中的元素无法被删除，不过可以使用 del 去删除整个元组 `del tup1`
### 运算符
- len() 返回元组长度
- value = tup1 + tup2 // 元组拼接
- value = tup1 * 2 // 元组重复
- in：判断元组中是否包含某个元素
### 内置函数
- len() 返回元组长度
- max() 返回元组中的最大值
- min() 返回元组中的最小值
- tuple() 将 list 转化为 tuple
## 字典 dict
dict1 = {1：“1”，2：“2”}

等同于其它编程语言中的 map

可使用字面量创建：
```py
dict1 = {1:"1","2":"2"} // dict 的key可以不是同一个类型的
```
也可以使用关键字 dict 创建字典

```py
dict1 = dict()
```
也是使用中括号访问 key 的 value 值 `dict1[1]` 同样的方法修改值 `dict1[1] = "2"`

使用 del 删除 dict 中的元素或者 dict 本身 `del dict1[1]` `del dict1`

使用 dict.clear() 来讲字典清空

dict 的 key 要求是唯一的，不能重复，并且可比较的，不能是变化的，所以应该使用数字，字符串，或者元组，使用 list 不行，因为 list 可，使用另一个 dict 当做 key 也不行，因为 dict 可变

### 内置函数
- len() 返回 dict 长度
- str() 返回 dict 的字符串表示
- type() 返回 dict 的类型
### 内置方法
- dict.clear() 清空 dict
- dict.copy() 复制 dict
- dict.fromkeys() 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
- dict.get() 返回指定键的值，如果值不在字典中返回默认值
- key in dict 判断 dict 中是否有 key
- dict.items() 返回 dict 的键值对组成的列表
- dict.keys() 返回 dict 的键的列表
- dict.setdefault() 如果指定键的值不在字典中，将会添加键值对
- dict.update(dict2) 把字典 dict2 的键/值对更新到 dict 里
- dict.values() 返回 dict 的值的列表
- pop() 返回指定键的值，并删除该键值对
- popitem() 返回并删除字典中的最后一对键值对
## 集合 set
一个无序不重复元素序列，可以理解为 dict 的 key

`set1 = {1,1.0,true,"1.0"} ` 看到了吧，是大括号，不是 list 的中括号也不是元组的小括号

也可以使用 set 的方式从 list 中创建 set `set1 = set([1,1.0,true,"1.0"])`

## 内置方法
- s.add(obj) 向集合中添加元素
- s.update(seq) 更新集合，添加 seq 中的元素，seq 为列表，元组，字典，set
- s.remove(obj) 删除指定元素，如果元素不存在，则抛出异常
- s.discard(obj) 删除指定元素，如果元素不存在，则不抛出异常
- s.pop() 删除并返回集合中的随机一个元素，如果集合为空，则抛出异常
- len() 返回集合长度
- s.clear() 清空集合
- x in s 判断元素是否在集合中
## 条件语句
### if
```py
if condition:
    do something
elif condition:
    do something
else:
    do something
```
```py
a = 12
if a > 10:
    print("a > 10")
elif a < 10:
    print("a < 10")
else:
    print("a == 10")
```
### match
这个 match 其实就是其它编程语言中的 switch
```py
match a:
    case 1:
        print("a == 1") 
        break
    case 2:
        print("a == 2")
        break
    case _:
        print("a != 1 and a != 2")
```

## 循环语句
### while
python 中的 while 跟 go 中的 for 是一个意思

```py
while condition:
    do something
```
```py
n = 100
while n > 0:
    print(n)
    n -= 1 
```
### for-in
Python 中的 for 循环实际上是 for range 的意思
```py
for i in range(10):
    print(i)
```
```py
a = "hello world"
for i in a:
    print(i)
```
## 推导式

## 迭代器

## 生成器

## 函数

## lambda

## 装饰器

## 模块

## 异常处理

## 面向对象编程

## 命名空间

## 作用域

## 输入输出

## file

## os

## 并发编程

