# coding:utf-8

class Test(object):
    def __str__(self):
        return 'this is str'

    def __getattr__(self, item):
        return '这个key {} 不存在' .format(item)

t = Test()
print(t)
print(t.a)


class Test1(object):
    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __call__(self, *args, **kwargs):
        print('args is {}'.format(kwargs))

    def __getattr__(self, item):
        return '这个key {} 不存在' .format(item)

t = Test1()

t.name = 'whldk'

print(t.name)

t(name='whldk')

print(t.f)

# 链式操作
class Test2(object):
    def __init__(self, attr):
        self.__attr = attr

    def __getattr__(self, key):
        if self.__attr:
            key = '{}.{}'.format(self.__attr, key)
        else:
            key = key
        print(key)
        return Test2(key)

    def __call__(self, name):
        return name

t2 = Test2('')

print(t2.sex.age(11))