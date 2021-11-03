# bicycle = ['trek','cannondale','redline','specialized']
# print(bicycle[0])
# print(bicycle[0].title())
# print(bicycle[-1])

# message = f"My first bicycle was a {bicycle[0].title()}"
# print(message)
# for x in range(0,4):
#     {
#         print(bicycle[x].title())
#     }

# motorcycle = ['honda','yamaha','suzuki']
# print(motorcycle)
# motorcycle[0] = 'ducati'
# print(motorcycle)
# motorcycle.append('honda')
# print(motorcycle)

# motorcycle = []
# motorcycle.append('ducati')
# motorcycle.append('honda')
# print(motorcycle)

# motorcycle = ['honda','yamaha','suzuki']
# motorcycle.insert(0,'ducati')
# print(motorcycle)
# motorcycle.remove('ducati')
# print(motorcycle)
# del motorcycle[0]
# print(motorcycle)
# popped_motorcycle = motorcycle.pop()
# print(motorcycle)
# print(popped_motorcycle)

# motorcycle = ['honda','yamaha','suzuki','ducati']
# too_expensive = 'ducati'
# motorcycle.remove(too_expensive)
# print(f"\nA {too_expensive} is too expensive for me")
# print(motorcycle)

# exercise
dinner_guest = ['A','B','C','D']
print(f"Guests who can come are:{dinner_guest}")
dinner_guest_poped = dinner_guest.pop(0)
print(f"Sorry the guest {dinner_guest_poped} can not come over")
dinner_guest.append('E')
print(f"Guests who can come now are:{dinner_guest}")
dinner_guest.insert(0,'F')
dinner_guest.insert(-1,'G')
dinner_guest.insert(3,'H')
print(dinner_guest)