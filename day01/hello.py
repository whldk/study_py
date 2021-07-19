
print("Hello, World!")

a = 10
b = 20
c = 30
d = 'ldk'

print(a + b + c)

if (a == b):
    print(a+b)
else:
    print(a+c)


print(d[0:3]);

print("ldk" not in d)

print(r'\n')

print(R'\n')

print("我今年%d岁, 我叫%s" % (b, d))

e = 'abcdabcdacf'

print( e.count('a') )

print( e*3 )

print( 'helo %s' % e)

print("""
这是一个多行字符串的实例
多行字符串可以使用制表符
""")

print(e.capitalize())

print(e.center(100,'*'))

str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))

print(str.endswith('教程'))

str_tab = "l\td\tk"

print(str_tab)

print(str_tab.expandtabs(1))
print(e.find('f'))

print(e.index('f'))

print(e.encode())

str = "this is string example....wow WOW!!!"

arr = str.split()
print(str.split())

print(len(arr), arr[0])

print(str.swapcase())

print(str.title())

str = "this is string example....wow WOW!!!"

intab = "aeiou"

outtab = "12345"

trantab = str.maketrans(intab, outtab)

print(trantab)

print(str.translate(trantab))

print(str.upper())

print(str.casefold())

print(str.lower())

print(str.zfill(100))

print(2**10)

print(10 / 3)

if (n := len(str) > 10):
    print(str)


a = 60

b = 13

# a&b = 0000 1100
#
# a|b = 0011 1101
#
# a^b = 0011 0001
#
# ~a  = 1100 0011

print(1 & 1)

print(1 | 1 | 1)
#
print(1 ^ 0)
#
# print(~a)
#
# print(2 << 9)
#
# print(2 >> 10)

a = [1,2,3]

print(a[:])

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)

if 'Taobao' in sites:
    print('yes')
else:
    print('no')

a = set('abcdedf')
b = set('abcghj')

#print(a)

print(a & b)  #交集

print(a | b)  #并集

print(a - b)  #差集

print(b -a)  #差集


dict = {}


tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

dict['one'] = 1
dict[2] = 2

print(dict)

tuple = ('a', 'b', 'c')

print(tuple)

a = '1'
print(int(a))

print(float(a))

print(complex(a))