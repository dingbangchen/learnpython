# python 列表脚本操作符
# print([1,2,3])
# print([1,2,3]+[4,5,6])
# print(['Hi!']*4)
# print(3 in [1 ,2 ,3])
# for x in [1,2,3]:
#     print(x)

# #python 列表截取
# L = ['Googel', 'Runnob', 'Taobao']
# print(L[2])
# print(L[-2])
# print(L[1:])
# L.append('FRED')
# L.append('RACHEL')
# print(L)
# #删除列表元素
# list1 = ['physics','chemistry',1997,2000]
# print(list1)
# del list1[2]
# print("After deleting value at index 2:")
# print(list1)

# python列表函数&方法
# cmp(list1, list2)
#     比较两个列表的元素
# len(list)
#     列表元素个数
# max(list)
#     返回列表元素最大值
# min(list)
#     返回列表元素最小值
# list(seq)
#     将元组转换为列表
# list.append(obj)
#     在列表末尾添加新的对象
# list.count(obj)
#     统计某个元素在列表中出现的次数
# list.extend(seq)
#     在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj)
#     从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj)
#     将对象插入列表
# list.pop([index=-1])
#     移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj)
#     移除列表中某个值的第一个匹配项
# list.reverse()
#     反向列表中元素
# list.sort(cmp=None, key=None, reverse=False)
#     对原列表进行排序


#元组
# #example
# tup1 = ('physics','chemistry,1997,2000')
# tup2 = (1,2,3,4,5)
# tup3 = "a","b","c","d","e"

#创建空元组
# tup1 = ()

#元组中只包含一个元素时，需要在元素后面添加逗号
# tup1 = (50,)

#访问元组
# tup1 = ('physics','chemistry',1997,2000)
# tup2 = (1,2,3,4,5,6,7,8,9,)
# print("tup1[0]: ", tup1[0])
# print("tup2[1:5]:", tup2[1:5])

# #元组中的元素是不允许修改的，但是我们可以对元组进行连接组合
# tup1=(12,34,56)
# tup2 = ('abc','xyz')
# tup3 = tup1+tup2
# print(tup3)

# #元组中的元素值是不允许被删除的，但是可以删除整个元组
# tup1 = ('physics','chemistry',1997,2000)
# print(tup1)
# del tup1
# print(tup1)

