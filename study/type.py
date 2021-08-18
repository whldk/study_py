# coding:utf-8




#标准类型六个标准的数据类型

# number 、string 、 list 、 tuple 、  set 、 dictionary
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）

str1 = 'hello python'
str2 = 'study'

num1 = 100
float1 = 100.00

a = b = c = 1

list1 = ['a', 'b', 'c']

# 中括号是 [] list， () 小括号 元组 ， 集合、字典是大括号 { }
print(list1)
print(list1[1])

tuple1 = ('a', 'b', 'c')
print(tuple1)

# 会删除重复的元素， 可以使用大括号 { } 或者 set() 函数创建集合,创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
set1 = {1,2,3,4,5,1,2}
print(set1)

# 字典 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict1 = {'name':'ldk', 'age':'18'}
print(dict1['name'])

#新增
dict1['sex'] = 'boy'
print(dict1)

#删除

#del dict1['name']  删除单个key

#dict1.clear()  清空

#del dict1  强制删除

print(dict1)

dict2 = {'name':[1,2,3,4], 'key':{'name':'age'}}

print(dict2)