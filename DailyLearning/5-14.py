

# a = 'babdc'
# b = 'abbdc'
# dict= {}

# for item in a:
#     dict[item] = 1+dict.get(item,0)

# print(dict)

def TwoSum(nums,target):
    dict = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in dict:
            return[dict[diff],i]
        else:
            dict[n] = i 


TwoSum(nums=[2,7,11,34],target=9)