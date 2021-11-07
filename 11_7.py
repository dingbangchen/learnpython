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