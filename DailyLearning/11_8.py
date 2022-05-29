#nesting:

# # a list of dictionary
# alien_0 = {'color':'green','points':5}
# alien_1 = {'color':'yellow','points':10}
# alien_2 = {'color':'red','points':15}
# aliens = [alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)

# # automatic generate alien
# aliens = []
# # create 30 green alien
# for alien_number in range(30):
#     new_alien = {'color':'green','point':5}
#     aliens.append(new_alien)
# # show the first five alien
# for alien in aliens[0:5]:
#     print(alien)
# # show hom many aliens has been created
# print(len(aliens))
# # modify each alien individually
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'red'
#         alien['point'] = 5
#         # we can also use elif for expanding
#     elif alien['color'] == 'red':
#         alien['color'] = 'yellow'
#         alien['point'] = 10
#     print(alien)
# print(aliens[0:5])

pizza = {
    'crust':'thick',                             #字典中间的逗号不要忘了
    'toppings':['mushroom','extra cheese']
}
# Summarize a pizza
print(f"Your order a {pizza['crust']}-crust pizza")
print("With the following topping")
for topping in pizza['toppings']:
    print(f"Your topping is {topping}")