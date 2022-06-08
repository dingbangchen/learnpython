
nums = [1,2,3,1,2,1,4,5,4,4] 
k = 2

count = {}
frequency = [[] for i in range(len(nums)+1)]

for n in nums:
    count[n] = 1 + count.get(n,0)
    print(count)
for n, c in count.items():
        frequency[c].append(n)
        print(frequency)
result=[]
for i in range(len(frequency)-1,0,-1):
    for n in frequency[i]:
        result.append(n)
        print(result)