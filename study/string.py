# coding:utf-8

'''
    python 中的 字符串的用法和常用函数 归纳
    可以使用 ' 或 " 来创建字符串
'''

var1 = 'hello'
var2 = "Python"

'''
    python 访问字符串 可以用方括号 [] 来截取字符串
    变量[头下标:尾下标]
    索引值以 0 为开始值  -1为从末尾开始的位置
'''
print(var1[0:2], var1[:2], var1[2], var1[2:], var1 +' '+ var2)

'''
    转义字符
    \ 续行符
    \\ 反斜杠符号
    \' 单引号
    \" 双引号
    \a 响铃
    \t , \n , \r 等待
'''

print("\n")


'''
    python 字符串运算符
    +  字符串连接
    *  重复输出字符串 a*10
    [] 通过索引获取字符串中的字符
    [:] 截取字符串中的一部分,遵循左闭右开原则 str[0:2]  返回 0,1
    in 成员运算符
    not in  成员与算符 跟 in 相反
    r/R 原始字符串
    %   格式字符串
'''

print(var2[0:2])


print('a + b: ', var1 + var2)

print('a * 2', var1*2)

print('a[1] ',  var1[1])

print('a[1:4]', var1[1:4])

if ('h' in var1):
    print('in')
else:
    print('not in')

print(r'\n')
print(R'\n')


'''
    Python 字符串格式化
    字符串格式化使用与 C 中 sprintf 函数一样的语法
    更多的查询官网
    %s 、 %d、 %c、 %f、%o、 %u、 %e
'''

print("我叫 %s  今年 %d 岁" % ('小米', 11))

'''
    python string 字符串 常用函数
'''
print(var1.capitalize()) # 首字符大写
print(var1.count('l', 1,  5))  #  统计字符串里某个字符出现的次数 count(str, start, end)

str_utf8 = var1.encode('UTF-8')     # decode 解码
print(str_utf8.decode())

print(var1.endswith('o'))  #  检查字符串是否以 指定字符串 结束  endswith(obj, start, end)


print(var1.isalnum()) #如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False

print(var1.isalpha()) #如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False

print(var1.isdigit())  #如果字符串只包含数字则返回 True 否则返回 False..

print(var1.islower(), var2.islower()) #字符都是小写，则返回 True，否则返回 False

print(var1.isnumeric()) #如果字符串中只包含数字字符，则返回 True，否则返回 False

print(var1.isspace()) #如果字符串中只包含空白，则返回 True，否则返回 False.

print(var1.isupper(), var2.isupper()) #字符都是大写，则返回 True，否则返回 False

s1 = '-'
print(s1.join(['1','2','3'])) # str.join(sequence) 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

print(len(var1), len(var2)) # 返回字符串长度

print(var1.ljust(40, '*'))  # 填充至长度 width 的新字符串
print(var1.rjust(40, '*'))   #返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
print(var1.center(40, '*')) #二边各自填充


print(var2.lower(), var2.upper()) #转换字符串中所有大写字符为小写

print(var1.lstrip('h')) #截掉字符串左边的空格或指定字符
print(var1.rstrip('o')) #截掉字符串右边的空格或指定字符
print(var1.strip('o')) #截掉字符串右边的空格或指定字符

'''
创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
'''
intab = 'hl'
outtabl = '12'
trantab = str.maketrans(intab, outtabl)
print(var1.translate(trantab))

print(max(var1), max(var2)) #返回字符串 str 中最大的字母
print(min(var1), min(var2)) #返回字符串 str 中最小的字母。
print(var2.replace('Python', 'php')) #把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次


print(var1.find('ll'))  # 查找字符串的位置 find(str, start, end)  -1 是不存在位置
print(var1.rfind('e'), var1.find('e')) #类似于 find()函数，不过是从右边开始查找.  返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
print(var1.index('l'), var1.rindex('l'))  # 跟find()方法一样 只不过如果str不在字符串中会报一个异常。

var3 = "Google#Runoob#Taobao#Facebook"
var4 = 'ab c\n\nde fg\rkl\r\n'
print(var3.split('#'), var4.splitlines())
#split 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
# splitlines() 按照行('\r', '\r\n', \n')分隔

print(var2.startswith('P'))
#检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。

print(var1.swapcase(), var2.swapcase()) #将字符串中大写转换为小写，小写转换为大写

print(var1.title(),var2.title()) #返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
print(var1.istitle(), var2.istitle()) #如果字符串是标题化的(见 title())则返回 True，否则返回 False

print(var1.zfill(40)) #返回长度为 width 的字符串，原字符串右对齐，前面填充0

print(var1.isdecimal()) #检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。