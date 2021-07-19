# import fibo
#
# a = fibo.fib(100)
#
# print(a)
#
# b = fibo.fib2(100)
#
# print(b)
#
# fib = fibo.fib
#
# fib(1000)


from fibo import fib, fib2

import fibo,sys

fib(500)


print(fib2(500))


for x in dir(sys):
    print(x)


print(dir())