# coding:utf-8
import math  # 导入数学函数类
import random  # 这是 随机函数类


'''
    Python 数字数据类型用于存储数值
    数据类型是不允许改变的，这就是意味着如果改变数字数据类型的值，将重新分配内存空间
'''

var1 = 1
var2 = 10

'''
    可以使用 del var1, var2 删除数字对象的引用
'''

del var1,var2

'''
    python 支持三种不同的数值类型
    整型      (int)   Python3 整型是没有限制大小的，可以当作 Long 类型使用
    浮点型    (float)  浮点型由整数部分与小数部分组成
    复数      (complex)   复数由实数部分和虚数部分构成
'''


'''
    Python 的数字类型转换
    有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可
    int(x)
    float(x)
    complex(x)
    complex(x, y)
'''

a = 1.0

print(int(a))

'''
    Python 数字运算
    表达式的语法很直白： +, -, * 和 /, 和其它语言（如Pascal或C）里一样
    
    在不同的机器上浮点运算的结果可能会不一样。
    在整数除法中，除法 / 总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 // ：
    
    / 会有余数
    // 返回整数
    
    ** 进行幕运算
'''

print( 10 / 3,  10 // 3, 10 // 2)

print(10 ** 8)

'''
    不同类型的数 混合运算时会将 整数 转换成 浮点数
'''

print( 3 * 3.75 / 1.5)

'''
    数学函数
'''

print(abs(-1)) #返回数字的绝对值，如abs(-10) 返回 10、
print(math.ceil(5.5))  #返回数字的上入整数，如math.ceil(4.1) 返回 5
print(math.exp(2)) #返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
print(math.fabs(-10)) #返回数字的绝对值，如math.fabs(-10) 返回10.0
print(math.floor(4.5)) #向下取整
print(max(1,2,3), min(1,2,3))
print(math.pow(10,8))
print(round(2.7355,2))
print(math.sqrt(7))

'''
    随机数函数
    随机数 可以用于 数学、游戏、安全等领域 ，还经常被嵌入到算法中、用以提高算法效率， 并提高程序的安全性
'''

print(random.choice(range(100))) #从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。


print(random.randrange(1,100,2)) #指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1

print(random.random()) #随机生成下一个实数，它在[0,1)范围内


random.seed(10) #改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。 有点看不懂这个seed
print(random.random())
list = [20, 16, 10, 5]
random.shuffle(list)
print(list)
random.shuffle(list)
print(list)


print(random.uniform(5,10)) #uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内。

