#迭代
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
#python的迭代循环抽象程度较高，所以也可以迭代dict
# d = {'a':1, 'b':2, 'c':3}
# for key in d:
#     print(key)
# #因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# #默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
# #由于字符串也是可迭代对象，因此，也可以作用于for循环：
# for value in d.values():
#     print (value)
# for k,v in d.items():
#     print (k,v)

#由于字符串也是可迭代对象，所以也可以作用于 for 循环
for ch in "ABC":
    print (ch)

#判断一个对象是否为可迭代对象
#通过 collctions.abc模块 的 iterable 类型来判断
from collections.abc import Iterable
print(isinstance('abc', Iterable))
print(isinstance(123,Iterable))
print(isinstance([1,2,3], Iterable))
#这里注意Iterable大写

#如果要像别的语言那样带下标循环
#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
L = [1,2,3,4,5,6,7,8,9,10]
for i , value in enumerate(L):
    print(i,value)
#这里注意一个小细节，L = []是创建一个list,L = list[]是将别的转化成list

#在for循环中创建有两个变量是非常常见的
for x,y in [(1,2),(3,4),(5,6)]:
    print (x,y)