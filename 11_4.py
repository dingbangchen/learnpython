# # tuples
# dimensions = (20,5)
# print(dimensions[0])
# print(dimensions[1])
# # this is wrong:
# # dimensions[0]=250
# # print(dimensions[0])

# # when we want to make a tuple with just one element:
# my_t = (3,)
# # don't forget the comma here

# for dimension in dimensions:
#     print(dimension)


# # Writing over a tuple
# dimensions = (200,5)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
# dimensions = (400,400)
# print("\nModified dimensions")
# for dimension in dimensions:
#     print(dimension)



# # Chapter 5 IF STATEMENT
# # Example
# cars = ['audi','bmw','subaru','toyota']
# for car in cars:
#     if car == 'bmw':     #pay attention to the double == here
#         print(car.title())
#     else:
#         print(car.upper())
    
# # ignoring case when ckecking for equality
# # case sensitive
# car = 'Audi'
# if car == 'audi':
#     print('True')
# else:
#     print('False\n')
# if car.lower() == 'audi':
#     print('True')
# else:
#     print('False\n')
# print(car)


# # check for inequality
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# answer = 42
# if answer != 17:
#     print("That is not the answer! try again")

# # check multiple conditions
# age_0 = 22
# age_1 = 18
# if (age_0 >=21) and (age_1>=21):
#     print('True')
# else:
#     print('False')

# # 尝试自己写一个function
# def agetest(age_0,age_1):
#     if (age_0 >=21) and (age_1>=21):
#         print('True')
#     else:
#         print('False')
# agetest(22,22)

# # checking whether a value is in a list
# requested_topping = ['mushrooms','onions','pineapple']
# if 'mushrooms' in requested_topping:
#     print('Ture')
# # Check If a value is not in the list
# if 'pepperoni' not in requested_topping:
#     print('True')


# # Boolean Expression
# car = 'subaru'
# print('Is car equal to subaru?, I predict True')
# print(car == 'subaru') # 注意这里条件判断输出还是要用print
# print('Is car equal to audi? I predict False')
# print(car == 'audi')

# def age_test(age):
#     if age < 4:
#         print("Your admission cost is $0")
#     elif age < 18:
#         print("Your admission cost is $25")
#     else: 
#         print('Your admission cost is $40')

# age_test(12)
# age_test(3)
# age_test(22)


# # !!! Using multiple elif blocks
# def age_test2(age):
#     if age < 4:
#         price = 0    #注意这里不能使用$符号！！
#     elif age <18:
#         price = 25
#     elif age < 65:
#         price = 40
#     else:   
#         price = 0
#     print(f"Your admission cost is ${price}")   #注意这里的print是在age_test2的方程里面的，不要弄错了缩进
# age_test2(12)

#testing multiple conditions
# toppings = ['mushrooms','pepperoni','extra chesse']
# if 'mushrooms' in toppings:
#     print('Adding mushrooms')
# if 'pepperoni' in toppings:
#     print('Adding pepperoni')
# if 'extra cheese' in toppings:
#     print('Adding extra cheese')


# # combine list with if statement
# toppings = ['mushrooms','green peppers','extra cheese']
# for topping in toppings:
#     print(f"Add {topping}")
# print('finished')

# # check that a list is not empty
# toppings = []
# if toppings:
#     for topping in toppings:
#         print(f"add {topping}")
# else:
#         print("Are you sure you want a plain pizza?")


# using multiple lists
available_toppings = ['mushrooms','olives','green peppers','pepperoni','[pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
       print(f"Adding {requested_topping}")
    else:
        print(f"Sorry we don't have {requested_topping}")
print('\nFinished making your pizza!')
# 这个代码后期重点看一下，涉及到for 和 if两个循环，需要弄清楚参数
    