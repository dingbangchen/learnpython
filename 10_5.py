# # 函数参数检查
# def abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operate type')
#     if x > 0:
#         return x
#     else :
#         return -x

# 返回多个值 计算坐标
# import math
# def move(x,y,step,angle = 0):
#     nx = x + step * math.cos(angle)
#     ny = y + step * math.sin(angle)
#     return nx,ny
# x,y = move(100,100,60,math.pi/6)
# print(x,y)

# import math
# print(math.sqrt(2))
import math


# import math
# def quadratic(a,b,c):
#     if b**2 - 4*a*c < 0: 
#         raise ValueError("Error")
#     x = (-b+math.sqrt(b**2 - 4*a*c))/2*a
#     return x
# r = quadratic(1, 3, -4)
# print(r)

# def power(x):
#     return x*x
# print(power(5))
# print(power(25))

# def power(x,n):
#     s = 1
#     while n > 0:
#         n = n-1
#         s = s*x
#     return s
# print(power(5,3))
# 这里很聪明的用了while循环来多次乘，没有直接使用指数符号

# 默认参数
# def power(x,n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s* x
#     return s
# print(power(5))
# print(power(5,n=3))
# 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
# 当不按顺序提供部分默认参数时，需要把参数名写上。
# def add_end(L=[]):
#     L.append('END')
#     return L
# print(add_end([1,2,3]))
# print(add_end(['x','y','z']))
# print(add_end())
# print(add_end())
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#定义默认参数要牢记一点：默认参数必须指向不变对象！
#修改
# def add_end(L = None):
#     if L is None:
#         L = []
#         L.append('END')
#         return L 
# print(add_end())
# print(add_end())

#可变参数
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n*n
#     return sum
# print(calc([1,2,3]))
# print(calc([1,2,5,7]))

#在使用之前需要先组装一个list 或 tuple
#将函数的参数改为可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc(1,2,3))