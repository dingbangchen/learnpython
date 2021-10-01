# print ("hello world")

# print('The quick brown fox', 'jumps over', 'the lazy dog', sep=",")

# name = input()
# print(name)

# name = input('please enter your name: ')
# print('hello', name)

# print("I\'m \"OK\"")

# print('''line1 
# ... line2
# ... line3''')

# 但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。

# print(10/3)
# print(10//3)
# print(10%3)

# print(ord('A'))
# print(ord('中'))
# print(chr(65))

# print('Hello, %s' % 'world')
# print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

# print('Age: %s. Gender: %s' % (25, True))
# print( 'growth rate: %d %%' % 7)

# r = 2.5
# s = 3.14 * r ** 2
# print(f'The area of a circle with radius {r} is {s:.2f}')

# classmate = ['Michael', 'Bob', 'Tracy']
# print(classmate[0])
# print(classmate[1])
# print(classmate[2])
# classmate.append('Adam')
# print(classmate)
# classmate.insert(1,'Jack')
# print(classmate)
# classmate.pop(1)
# print(classmate)
# classmate.pop()
# 'Adam'
# print(classmate)
# classmate[1]='Sarah'
# print(classmate)

# L = ['Apple', 123, True]

# p = ['asp', 'php']
# s = ['python', 'java', p, 'scheme']
# print(s[2][1])


# age = 20
# if age >= 18:
#     print('your age is: ', 18)
#     print('adult')

# age = 13
# if age >= 18:
#     print('your age is : ', age)
#     print('Adult')
# else:
#     print('your age is : ', age)
#     print('Teenager')

# age = 3
# if age >= 18:
#     print('Adult')
# elif age <= 6:
#     print('kid')
# else:
#     print('teenager')

age = input("age :")
ages = int(age)
if ages >= 18:
    print('adult')
elif ages <= 6:
    print('kid')
else:
    print('teenager')

