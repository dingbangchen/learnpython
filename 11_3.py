# # Sorted() Function
# cars = ['bmw','audi','toyota','subaru']
# print('Here is the original list')
# print(cars)
# print('\nHere is the sorted sorted list:')
# print(sorted(cars))
# print('\nHere is the original list again:')
# print(cars)
# print('\nHere is the reversed list')
# cars.sort(reverse=True)
# print(cars)
# print('\nHere we can reverse again')
# cars.reverse()
# print(cars)
# print('\nHere is the length of the list')
# print(len(cars))



# # Loop through a list
# magicians = ['alice','david','carolina']
# for magician in magicians:
#     print(magician)
#     print(f"{magician.title()}, that was a great a trick")
#     print(f"I can wait to see your next trick, {magician.title()}")
# print('\nThank you everyone, that was a great show')


# Making Numerical lists
for values in range(1,5):
    print(values)

# # Use range to make a list of numbers
# numbers = list(range(1,6))
# print(numbers)

# even_number = list(range(2,11,2))
# print(even_number)
# odd_number = list(range(1,12,2))
# print(odd_number)
# # better explain about steps: https://www.learnbyexample.org/python-list-slicing/

# squares = []
# slide = list(range(1,11))
# print(slide)
# for n in slide:
#     square = n ** 2
#     print(square)
#     squares.append(square)
# print(squares)

# better way:
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)