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


import math
def quadratic(a,b,c):
    if b**2 - 4*a*c < 0: 
        raise ValueError("Error")
    x = (-b+math.sqrt(b**2 - 4*a*c))/2*a
    return x
r = quadratic(1, 3, -4)
print(r)