# coding:utf-8

"""
    常用的异常类型集合
    :exception 通用异常类型（基类）
    :ZeroDivisionError 不能为0
    AttributeError 对象没有这个属性
    IOError 输入输出


    自定义抛出异常函数 --raise
    用法：
     raise 异常类型（msg）

"""

def test():
    try:
        print("upupup")
    except (ZeroDivisionError, NameError) as e:
        print(e)
    except Exception as e:
        print(e)
    except (AttributeError, ValueError, IOError,KeyError, TypeError) as e:
        print(e)
    finally:
        print('eee')




def test1(num):

    if num == 100:
        raise ValueError('num not eq 100')
    return num


ras = test1(50)


def test2(num):
    try:
        return test1(num)
    except ValueError as e:
        return e


re = test2(100)

print(re)



class NumLimitError(Exception):
    def __init__(self, msg):
        self.msg = msg


class NameLimitError(Exception):
    def __init__(self, msg):
        self.msg = msg

def test5(name):
    if name == 'ldk':
        raise NameLimitError('ldk no no')
    return name


def test6(num):
    if num > 100:
        raise NumLimitError('num > 100')
    return num

print('--------------')

try:
    test5('ldk')
except NameLimitError as e:
    print(e)

try:
    test6(101)
except NumLimitError as e:
    print(e)


test6(100)