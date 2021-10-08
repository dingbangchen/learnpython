# #元组运算符
# print(len((1, 2, 3)))
# print((1, 2, 3) + (4, 5, 6))
# print(('Hi!',) * 4)
# print(3 in (1, 2, 3))
# for x in (1, 2, 3): 
#     print(x)

# #元组索引，截取
# L= ("spam","Spam","SPAM")
# print(L[1])
# print(L[-2])
# print(L[1:])

#任意无符号的对象，以逗号隔开，默认为元组
print('abc',-4.23e93,18+6.6j,'xyz')
x,y = 1,2
print('Value of x,y', x,y)

#元组内置函数
比较两个元组元素
    cmp(tuple1,tuple2)
计算元组元素个数
    len(tuple)
返回元组中元素最大值。
    min(tuple)
将列表转换为元组。
    tuple(seq)