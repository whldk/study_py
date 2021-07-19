
# 多继承
#
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     <statement-N>
#需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。


class people:
    name = ''
    age = 0

    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说： 我 %d 岁。" %(self.name, self.age))



class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


class sample(speaker, student):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample('Tim', 25, 80, 4, 'python')

test.speak()



class Parent:
    def myMethod(self):
        print('调用父类方法')

class Child:
    def myMethod(self):
        print('调用子类方法')


c = Child()
# 子类实例
c.myMethod()
# 子类调用重写方法
# #super(Child,c).myMethod()
#用子类对象调用父类已被覆盖的方法


#全局
var1 = 5

def test1():
    var2 = 6
    def test2():
        var3 = 7


class Test:
    def __init__(self):
        print('init')

    def __del__(self):
        print('del')





num = 1

def fun1():
    global num
    print(num)
    num = 123
    print(num)

fun1()
print(num)





