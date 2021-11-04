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

# check multiple conditions
age_0 = 22
age_1 = 18
if (age_0 >=21) and (age_1>=21):
    print('True')
else:
    print('False')

# 尝试自己写一个function
def agetest(age_0,age_1):
    if (age_0 >=21) and (age_1>=21):
        print('True')
    else:
        print('False')
agetest(22,22)