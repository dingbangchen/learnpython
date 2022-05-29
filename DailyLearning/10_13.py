#列表生成式
#https://www.cnblogs.com/yyds/p/6281453.html
#列表生成式的基础语法
#[exp for iter_var in iterable]
#迭代iterable中的每个元素；
#每次迭代都先把结果赋值给iter_var，然后通过exp得到一个新的计算值；
#最后把所有通过exp得到的计算值以一个新列表的形式返回。

#列表生成启动的过滤用法
# [exp for iter_var in iterable if_exp]# L = []
#迭代iterable中的每个元素，每次迭代都先判断if_exp表达式结果为真，如果为真则进行下一步，如果为假则进行下一次迭代；
#把迭代结果赋值给iter_var，然后通过exp得到一个新的计算值；
#最后把所有通过exp得到的计算值以一个新列表的形式返回。

#循环嵌套语法格式
#[exp for iter_var_A in iterable_A for iter_var_B in iterable_B]





print(list(range(1,11)))

print([x * x for x in range(1,11)])
#这里记得要加上放括号
#这里把要生成的元素先放出到前面然后后面跟for循环就能创建list了

#for循环后面还可以加if语句
print([x*x for x in range(1,11) if x%2 == 0])
#这里还是要注意方括号和双等号

#双层循环
print([m + n for m in 'ABC' for n in 'BCD'])

#for循环可以同时迭代多个变量
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for m,k in d.items():
    print(m,'=',k)

#计算两个集合的全排列
di = {'a': 'A', 'b': 'B','c':'C'}
print([x + '=' + y  for x,y in di.items()])
#这里注意是加号并且 dict里面是string，如果想要输出数字的话需要用括号

#把所有字符小写
L = ['AppLE','gOOGLE','FACEBOOK']
print([s.lower() for s in L])