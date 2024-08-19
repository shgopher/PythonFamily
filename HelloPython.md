<!--
 * @Author: shgopher shgopher@gmail.com
 * @Date: 2024-08-18 11:41:33
 * @LastEditors: shgopher shgopher@gmail.com
 * @LastEditTime: 2024-08-19 17:16:33
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
- list 就是不同类型的切片 [1,1.0,true，“1.0”]，跟元组也不一样，元组虽然是不同类型的，但是元组的元素不能修改，list 可以修改，所以你可以理解为它是不同类型的切片，或者一个只拥有 key 的 map

