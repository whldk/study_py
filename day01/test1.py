#
# s = 'Hello Ldk'
#
# print(str(s))


# dict = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
#
# for key, val in dict.items():
#     print('{0:5} ==> {1:2d}'. format(key,val))

try:
    x = int(input('请输入参数值:'))
    raise ValueError('hi')
except ValueError:
    print(2)
except OSError:
    print(3)
except IOError:
    print(4)
except ImportError:
    print(5)
except NameError:
    print('hi')
except:
    #默认异常
    print(6)
else:
    #没有异常时执行的代码
    print(7)
finally:
    # 不管有没有异常都会执行的代码
    print(8)