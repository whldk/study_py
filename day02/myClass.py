
# 类定义
class myClass:

    # 定义基本属性
    i = 123

    # 定义私有属性、私有属性在类外部无法直接进行访问
    __zs = 'zhangshuai'

    # 定义构造方法
    def __init__(self, xxx):
        print(self.f())
        print(xxx)

    # 定义普通方法
    def f(self):
        return  'hello'


# 继承类

class youClass(myClass):
    grade = 0

    def __init__(self, xxx, grade):
        #调用父类的构造函数
        myClass.__init__(self, xxx)
        self.grade = grade

    # 覆盖父类的方法
    def ff(self):
        return  self.grade


# x  = myClass('init')
#
# print(x.i)
#
# print(x.f())

y = youClass('init', 2021)

print(y.ff())


#global 和 nonlocal关键字








