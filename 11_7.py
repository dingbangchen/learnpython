# # Dictionary
# alien_0 = {'color':'green','point':5 }
# print(alien_0['color'])
# print(alien_0['point'])

# new_values = alien_0['point']
# print(f"You just earned {new_values} points!")

# # set coordinate
# print(alien_0)
# alien_0['x_position'] = 0     #这里使用的是方括号，可以理解成还是添加了一个list的值
# alien_0['y_position'] = 25
# print(alien_0)

# # starting with empty dict
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['point'] =5
# print(alien_0)

# # modifying values in a dict
# alien_0 = {'color':'green'}
# print(f"the alien is {alien_0['color']}")
# alien_0['color'] = 'yellow'
# print(f"the alien is {alien_0['color']}")


# # track the position of the alien that can move at different speed
# alien_0={'x_position': 0, 'y_position':25, 'speed':'medium'}
# print(f"Original position is {alien_0['x_position']}")

# # move the alien to the right
# # determine how fat to move the alien based on the current speed
# if alien_0['speed'] == 'slow':                       #这里还是要注意等号的问题
#     x_increment = 1
# if alien_0['speed'] == 'medium':
#     x_increment = 2
# if alien_0['speed'] == 'fast':
#     x_increment = 3
# #the new position is the old position plus the increment
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position : {alien_0['x_position']}")

# # Removing key-value pairs
# alien_0 = {'color':'green','point':5}
# del alien_0['point']
# print(alien_0)
# # how to pop and remove?


# # A dictionary of similar object
# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil':'python',
# }
# # 注意这里的逗号不能忘了
# # to look up their favorite language
# language = favorite_language['sarah'].title()
# print(f"sarah's favorite language is {language}")

# # using get() to access values
# alien_0 = {'color':'green', 'point':5}
# print(alien_0['point'])
# # the get() method requires a key as a first argument, as the second optional argument, you can pass the value to be returned
# #if the key does't exist
# speed_value = alien_0.get('speed','slow')
# print(speed_value)



# # looping through a dictionary
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last':'fermi',
# }
# for key,value in user_0.items():
#     print(f"\nKey:{key}")
#     print(f"Value:{value}")

# looping through all key-value
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil':'python',
}
for name, language in favorite_language.items():         #这里注意要加item， dict object is not callable
    print(f"{name}'s favorite language is {language}")

# looping through all keys
for name in favorite_language.keys():
    print(name.title())
for name1 in favorite_language:
    print(name1.title())
# these two are exactly the same

# You can access the value associated with any key inside the loop by using the current key
friend = ['phil','sarah']
for name in favorite_language.keys():
    print(f"Hi,{name.title()}")
    if name in friend:
        language = favorite_language[name].title()
        print(f"\t{name}, your favorite language is {language}")

# you can also use the key() to find out if a particular person was polled
if 'erin' not in favorite_language.keys():
    print("Erin,please take our poll")


# looping through a dictionary's keys in a particular order
for name in sorted(favorite_language.keys()):
    print(f"{name}, thank you for taking the poll")



# looping through all values in a dictionary
print('The following language has been mentioned')
for language in sorted(favorite_language.values()):
    print(language.title())
for language in sorted(set((favorite_language).values())):
    print(language.title())

