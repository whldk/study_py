# coding:utf-8
import os

# python的数据类型


num1 = 1

float1 = 1.123

str1 = 'str'

# 列表用中括号表示， 索引从0开始 、列表可以进行的操作包括索引、切片、加减乘检查成员等等、常用的数据类型
list1 = ['whldk', 'whzs', 'whmw']


# 元组 用小括号表示 ()， 与列表相似，不同之处在于元组的元素不能修改 , 不需要括号 也可以创建
# 元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：

tuple1 = ('whldk', 'whzs', 'whmw')

tuple2 = 'whldk', 'whzs', 'whmw'


# 字典是可变容器模型，且可以存储任意类型对象
# 字典用大括号表示
# 键必须是唯一的，但值则不必, 值可以取任何数据类型，但键必须是不可变的，如字符串，数字

dict1 = {'name':'whldk', 'age': 25, 'sex': '男'}

#print(dict1)

# 集合 set  是一个无序的不重复的元素序列
# 可以使用 大括号 {} 或者 set() 函数创建集合, 创建空集合必须用 set()

set1 = {'1', '2', '3', 1}
set1.add(4)
#print(set1)
c = set('abcd')

c.update({1,3, '1', 4}, ['fd','e', 'a'])
#[1, 2, 3],  {1,2,3},  (1,2,3)

c.remove('fd')
c.discard('fd')  # 不存在也不会报错


d = c.union(set1)

def test():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(j, "*",i, '=', i*j, "\t", end='')
        print("\n")


#test()

count = 0
while (count != 5):
    count = count+1
    print('count', count)

f = lambda x, y = 2  : \
    x > y

#print(f(1))


users = [
    {'name': 'whldk'},
    {'name':'whzs'},
    {'name':'whmw'}
]

users.sort(key=lambda x:x['name'])

print(users)