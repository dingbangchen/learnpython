lista,listb=[],[]
for x in range(96,180):
    lista.append(x)
for y in range(1,13):
    listb.append(y)
for c in zip(lista,listb):
    print(c)
    input()