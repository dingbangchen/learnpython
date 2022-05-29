# lst = [1,2,3,4,5]

# # 求列表的长度
# print(len(lst))
# # 判断6 是否在列表中
# print(6 in lst)
# # lst + [6, 7, 8] 的结果是什么？
# print(lst+[6,7,8])
# # lst*2 的结果是什么
# print(lst*2)
# # 列表里元素的最大值是多少
# print(max(lst))
# # 列表里元素的最小值是多少
# print(min(lst))
# # 列表里所有元素的和是多少
# print(sum(lst))
# # 在索引1的位置新增一个的元素10
# lst[1]=10
# print(lst)
# # 在列表的末尾新增一个元素20
# lst.append(20)
# print(lst)




# lst = [1, [4, 6], True]
# 请将列表里所有数字修改成原来的两倍
# lst[0]=2
# lst[1][0]=8
# lst[1][1]=12
# print(lst)
# # using function
# def double_lst(lst):
#     for index,item in enumerate(lst):
#         if isinstance(item,bool):
#             continue
#         if isinstance(item,(int,float)):
#             lst[index] *= 2
#         if isinstance(item,list):
#             double_lst(item)

# lst = [1, [4, 6], True]
# double_lst(lst)
# print(lst)


lst_a = []
lst_b = []
a = range(1,4)
for i in a:
    lst_a.append(i)
lst_a = lst_a*4
print(lst_a)
b = range(1,13)
for d in b:
    lst_b.append(d)
for c in zip(lst_a,lst_b):
    print(c)