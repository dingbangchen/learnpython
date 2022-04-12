lista = [1,2,3]
# for element in lista:
#     print(element)

# x = iter(lista)
# print(x.__next__())
x = lista.__iter__()
print(next(x))
print(x)