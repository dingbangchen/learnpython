from itertools import product


A = [1,2,3,4]
B = [2,3,4,5]
for a in product(A,B):
    print(a)