from collections import defaultdict
s = "missippi"
d = defaultdict(int)
for k in s :
    d[k] += 1
d["m"]= 2
print(d.items())

# https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work