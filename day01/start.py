# a = 'string'
#
# b = 0.01
#
# c = ['a', 'b', 'c', 'd', 'e']
#
# d = (1,2,3,4,5)
#
# f = {1:1,2:2,3:3}
#
# e = {1,2,3,4,5}


# a, b = 0, 1
#
# while b < 1000:
#     print(b, end=',')
#     a, b = b, a+b



#a, b = b, a+b
# n=b
# m=a+b
# a=n
# b=m

# a = 1
# b = 2
# if a == b:
#     print(a + b)
# else:
#     print(a + b)
#
#
# age = int(input("请输入你家的狗多大了："))
# print("")
# if age <= 0:
#     print("居然这么大了：%d" % age)
# elif age == 15:
#     print("居然%d" % age + "大了")
# else:
#     print("你是在逗我吧!")
#
# ### 退出提示
# input("点击 enter 键退出")
#
# num = int(input("请输入一个数字："))
#
# if num%2 == 0:
#     if num%3 == 0:
#         print("2 and 3 can % 0")
#     else:
#         print("2 can % 0")
# else:
#     if num%3 == 0:
#         print("3 can % 0")
#     else:
#         print("2 and 3 not can % 0")
#
#
# input("点击 enter 键退出")

# number = 7
# guess = -1
# print("猜字谜")
# while guess != number:
#     guess = int(input("请输入："))
#     if guess == number:
#         print("yes")
#     elif guess < number:
#         print("小了")
#     else:
#         print("大了")


#a = 1

# while a < 100:
#     print(a)
#     a += 2
#
#     n = 100

# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum += counter
#     counter += 1
#
# print("1 到 %d 之和为: %d" % (n, sum))
#
# while 1 == 1:
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)

# print("Good bye!")
#
# languages = ["C", "PHP", "JAVA", "Python"]
#
# for x in languages:
#     print(x.upper())
#
#
# for i in range(5,100):
#     print(i)
#     if i == 9:
#         print(99 + 1)
#         continue
#     if i == 10:
#         print(100 - 1)
#         break

# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
#
# for i in range(0, 5):
#     print(i, a[i])
#
# print(tuple(range(5)))
#
# print(list(range(5)))
#
# for letter in 'Runoob':
#     if letter == 'o':
#         pass
#         print('执行 pass 块')
#     print('当前字母 :', letter)
#
# print("Good bye!")
#
# if None:
#     print('hello')
#
# it = list(range(5))
#
# ite = iter(it)

# print(ite)
#
# print(next(ite))
# print(next(ite))
# print(next(ite))
#
# for x in ite:
#     print(x)


import sys

# while True:
#     try:
#         print(next(ite))
#     except StopIteration:
#         sys.exit()

#
# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#       if self.a <= 20:
#         x = self.a
#         self.a += 1
#         return x
#       else:
#           raise StopIteration
#
# myClass = MyNumber()
#
# myiter = iter(myClass)
#
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
#
# for x in myiter:
#   print(x)

# def fibonacci (n):
#     a, b, counter = 0, 1 , 0
#     print(a, b, counter)
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
# f = fibonacci(10)
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()