# coding:utf-8

'''
    装饰器的定义与使用
    一种特殊的函数
    def a(func):
        def b(*args, **kwargs):
            return func(*args, **kwargs)
        return b

    def c(name):
        print(name)
    a(c('hello'))


    deg out(func_args)： 外围函数
        def inter(*args, **kwargs):     内嵌函数
            return func_args(*args, **kwargs)
        return inter

    decoratory 装饰器

    classmethod  将类函数可以不经过实例化而被调用
    staticmethod
    property

'''

def check_str(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 'ok':
            return 'result is %s' % result
        else:
            return 'result is %s' % result
    return inner

@check_str
def test(data):
    return data

# result = test('ok')
# print(result)
#
# result = test('none')
# print(result)


class Test(object):
    def __init__(self, a):
        self.a = a

    def run(self):
        print('run')
        self.go()
        self.sleep()

    @classmethod
    def go(cls):
        print('go')


    @staticmethod
    def sleep():
        print('sleep')


# t = Test('a')
# t.run()
# Test.go()
#
# Test.sleep()
# t.sleep()


class Test1(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


t1 = Test1(name='whldk')

#print(t1.name)

t1.name = 'test'

#print(t1.name)





class Parent(object):
    def __init__(self):
        print('parent')


class Child(Parent):
    def __init__(self):
        print('child')
        super().__init__()


if __name__ == '__main__':
    c = Child()














