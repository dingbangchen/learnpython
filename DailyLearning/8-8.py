# ## review for the dictionary and leetcode 242
# a = "babdc"
# dict={}
# for item in a:
#     dict[item] = dict.get(item,0) + 1
#     print(dict)
# print(dict)

cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 设置默认值，该key在dict中不存在，新增key-value对
print(cars.setdefault('PORSCHE', 9.2)) # 9.2
print(cars)
# 设置默认值，该key在dict中存在，不会修改dict内容
print(cars.setdefault('BMW', 3.4)) # 8.5
print(cars)