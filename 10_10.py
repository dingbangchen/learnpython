# #函数的参数
# def power(x):
#     return x*x
# print(power(2))
# print(power(5))

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name,age,**kw):
    print('name',name,'age',age,'other',kw)
print('Micheal',30)
print(person('Bob',35,city = 'beijing'))