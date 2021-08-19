# coding:utf-8

'''
    python 字典
    字典是另一种可变容器模型，且可储存任意类型对象
    字典的每个键值  key => value 对， 用冒号 ：分割  ，每个对之间用 , 号 分割， 整个字典包括在花括号 {} 中
    d = {key1 : value1, key2 : value2}

    健必须是唯一的，但值则不必
    值可以取任何数据类型， 但健必须是不可变的，如字符串、数字
'''


dict1 = {"abc":123}
dict2 = {"age":18, 'up':3}

print(dict1['abc'], dict2['up'])

'''
    修改字典
    向字典添加新内容的方法就是增加新的键值对，修改或者删除已有的键值对
'''

dict = {"name":"runoob", "Age":7, "class":'one'}

dict["Age"] = 8

dict['name'] = 'ldk'

del dict['class']

print(dict)


'''
    字典的特性
    字典值可以是任何的python对象， 既可以是标准的对象，也可以是用户定义的，但key 健不行
    1、不允许同一个健出现二次，如果出现二次，则后一个健会被记住
    2、健必须不可变、所以可以用数字、字符串、元组充当， 而列表就不行
    
    可变  : 字典、列表、集合
    不可变: 数字、字符串、元组
'''

dict1 = {"name":"zs", "name":'mw', ('1','2') : ['ww']}

print(dict)


'''
    字典内置函数 & 方法
    len(dict)        #计算字典元素个数，即键的总数
    str(dict)        #输出字典，可以打印的字符串表示
    type(variable)   #返回输入的变量类型
'''


'''
    字典内置方法
'''

dict.clear() #删除字典内所有元素
print(dict)

print(dict1.copy()) #返回一个字典的浅复制



seq = ('name', 'age', 'sex')

dict1 = dict.fromkeys(seq)

dict2 = dict.fromkeys(seq, 10) #创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值

print(str(dict1), dict2)

print(dict2.get('name')) #如果键在字典dict里返回true，否则返回false


print(dict2.items())  #以列表返回一个视图对象


print(dict1.keys())   #以列表返回一个视图对象

dict1.update(dict2)
print(dict1)

dict1.setdefault('hello') #和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default


dict1.pop('name')

print(dict1)

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj)
print(site)
