from turtle import left


list = "abcabcbbs"
left = 0
tem_store=[]
for right in range(len(list)):
    if list[right] in tem_store:
        left+=1
    else:
        tem_store.append(list[right])
print(right-left+1)