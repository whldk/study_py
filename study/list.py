# coding:utf-8

'''
    序列是 python 中最基本的数据结构
    列表可以进行的操作  包括（索引、切片、加、乘、检查成员）
    创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
'''

list1 = ['google', 'baidu', 2021]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'blue', 'yellow']

'''
    与字符串的索引一样、列表索引从0开始 
    通过索引列表可以进行截取、组合等操作
'''

print(list1[0])
print(list1[1])
print(list1[2])

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4])

#从第二位开始（包含）截取到倒数第二位（不包含）
print(nums[1:-2])

#可以对列表的数据项进行修改或更新，你也可以使用 append() 方法来添加列表项

nums[1] = 2020

print(nums)

nums.append(2021)

print(nums)

del nums[2]

print(nums)

'''
    Python 列表脚本操作符
    列表对 + 和 * 的操作符
    如下所示：
    len([1, 2, 3])        长度
    [1, 2, 3] + [4, 5, 6] 组合
    ['up'] * 3  =  ['up', 'up', 'up']
    3 in [1, 2 ,3] true 元素是否存在于列表中
    for x in [1, 2, 3]: print(x, end = "") 1 2 3 迭代
'''


'''
    python 列表截取与拼接
    L = ['google', 'Runoob', 'Taobao']
'''

L = ['google', 'Runoob', 'Taobao']

print(L[2])
print(L[-2])
print(L[1:])

print(list1 + list2)

# 列表拼接
s1 = [1,4,9]
s1 += [2,3,6]
print(s1)

'''
    嵌套列表
    使用嵌套列表即在列表里创建其他列表, 例如:
'''
a = ['a', 'b', 'c']
b = [1, 2, 3]
c = [a, b]
print(c)


'''
    python 列表函数 方法
    len(list)
    列表元素个数
    max(list)
    返回列表元素最大值
    min(list)
    返回列表元素最小值
    list(seq)
    将元祖转换为列表
'''

print(max(a), min(b))


'''
    python 包含以下方法
'''

list3.append('wocaonigejb') #在列表末尾添加新的对象
print(list3)

print(list3.count('a')) #统计某个元素在列表中出现的次数

print(len(list3))   #列表元素个数

list1.extend(['up', 'up']) #在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print(list1)


print(list1.index('up'))  #从列表中找出某个值第一个匹配项的索引位置

list1.insert(1, ['2.73', 'la', 'la']) #将对象插入列表

print(list1)


list1.pop(-3) #移除列表中的一个元素（默认最后一个元素），并且返回该元素的值  list.pop([index=-1])
print(list1)

list1.remove('google') #list.remove(obj) 移除列表中某个值的第一个匹配项
print(list1)


list2.reverse()  #反向列表中元素
print(list2)

list2.sort()    #对原列表进行排序
print(list2)

list2.clear() #清空列表
print(list2)

print(list1.copy()) #	list.copy()复制列表