#昨天函数部分还需要加强理解
#详细看https://www.zhihu.com/question/57726430

#递归函数
#在函数内部调用自身就是递归函数
# def fact(n):
#     if n == 1:
#         return n
#     return n*fact(n-1)

# print(fact(10))

#python 高级特性
#构造一个1到99的列表
# L = []
# n = 1
# while n <= 99:
#     L.append(n)
#     n = n + 2
# print(n)

# L =['A','B','C','D','E','F','G','H']
# # print([L[1],L[2],L[3]]) #笨办法
# #聪明办法
# # r = []
# # n = 3
# # for i in range(n):
# #     r.append(L[i])
# # print(r)
# #但是python直接提供了切片操作符
# print(L[0:3])
# #如果第一个索引是0还可以省略
# print(L[:3])
# #从倒过来开始数
# print(L[-2:])
# print(L[-2:-1])
# #记住！！倒数第一个元素的索引是[-1]

# #创建一个0-100的数列
# L = list(range(0,101))
# print(L)
# #前十个数字
# print(L[:10])
# #后十个数字
# print(L[-10:])
# #前11-20个数字
# print(L[10:20])
# #这里开始注意
# #前十个数，每两个取一个
# print(L[:10:2])
# #所有数，每5个取一个
# print(L[::5])

#元组也可以用切片的操作
# L =(0,1,2,3,4,5,6,7,8,9,10,11)
# print(L[0:3])

#字符串也可以看成是一个list
L = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(L[0:3])
print(L[::2])

