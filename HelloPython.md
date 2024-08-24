<!--
 * @Author: shgopher shgopher@gmail.com
 * @Date: 2024-08-18 11:41:33
 * @LastEditors: shgopher shgopher@gmail.com
 * @LastEditTime: 2024-08-24 23:04:42
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
## 字符串 string
## 列表 list
## 元组 tuple
## 字典 dict
## 集合 set
## 条件语句
## 循环语句
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

