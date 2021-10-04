# names = ['Micheal','Bob','Tracy']
# for name in names:
#     print(name)

# sum = 0
# for x in [1,2,3,4,5,6,7,8,9,10]:
#     sum = sum + x
#     print(sum)
# print(sum) 
# 注意这里在循环内还是循环外的区别

# print(list(range(88,101)))

# sum = 0
# for x in list(range(101)):
#     sum = sum + x
# print(sum)

#while loop
# sum = 0
# x = 99
# while x>0:
#     sum = sum + x
#     x = x -2
# print(sum)

# 小测试
# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#     print("Hello," + x)

# n = 1
# while(n<100):
#     if n > 10:
#         break
#     print(n)
#     n = n+1
# print('END')
# 注意这里的if判断条件，是n大于10 的时候退出

# n = 0
# while(n<10):
#     n = n +1
#     if(n%2 == 0):
#         continue
#     print(n)

# d = {'Michel':95, 'Bob': 75, 'Tracy': 85}
# print(d['Michel'])

# L = list(range(1,101))
# i = 0;
# while(i<100):
#     print(L[i])
#     i = i+2;
# 如果想获得奇数的话直接i = 1 就可以了

# d = {'Michel':95, 'Bob': 75, 'Tracy': 85}
# # print(d=['Thoems'])
# # print('Thoms' in d)
# # print(d.get('Thomes', 4)) 如果d里面的key不存在就返回一个自定值
# d.pop('Bob')
# print(d)

# s = set([1,2,3,3,4,4,5])
# print(s)
# s.add(4)
# print(s)
# s.add(6)
# print(s)
# s.remove(4)
# print(s)
# s1 = set([1,2,3])
# s2 = set([2,3,4])
# print(s1&s2)
# print(s1|s2)

# a = ['c','b','a']
# a.sort()
# print(a)
# 注意这里不能直接print(sort)因为这样优先进行的print但是无法sort

# a = 'abc'
# a.replace('a','A')
# print(a)
# b= 'abc'
# b.replace('a','A')
# print(b,a)

# 列表 list[] 、元组 tuple() 、字典 dict{ key : value } 、无序不重复元素集合 set(list[]) ，后两者的key为不可变对象。元组也不可变。