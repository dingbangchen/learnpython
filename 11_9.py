# continue of Dictionaries
# # A Dictionary in a dictionary
# # User for the website
# user = {
#     'user_1' :{
#         'first':'albert',
#         'last':'einstein',
#         'location':'princeton',
#     },      #这里的逗号不要忘了
#     'user_2' :{ 
#         'first':'marie',
#         'last':'curie',
#         'location':'paris',
#     }
# }
# for username, userinfo in user.items():
#     print(f"\nusername:{username}")
#     fullname = f"{userinfo['first']} {userinfo['last']}"
#     print(f"fullname is {fullname.title()}")
#     print(f"location is {userinfo['location'].title()}")




# USER INPUT AND WHILE LOOP
# # How the input() function works
# message = input("Tell me something, and I will repeat it back to you:\n ")
# print(message)

# # Write a prompt that is longer than one line
# prompt = "If you tell us who you are, we can personalize the message you see."
# prompt += "\nWhat is your first name?\n"
# name = input(prompt)
# print(f"Hello,{name}")

# # using int() to accept numerical input
# age = input("how old are you")
# print(age)      #here it is actually a string
# # if we want to compare
# age = int(age)
# print(age >=18)

# # real life example
# height = input("please enter your height")
# height = int(height)

# if height <= 48:
#     print("You are not tall enough to do this")
# else:
#     print("Welcome")

# # The modulo operator
# print(4%3)
# print(5%3)
# print(6%3)
# print(7%3)

# # EVEN AND ODD test
# number = input("tell me a number and I will tell you it is even or odd\n")
# number = int(number)
# if number%2 == 0:
#     print("This is a even number")
# else:
#     print("This is a odd number")   



# WHILE LOOP
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# # let the user choose when to quit
# prompt = '\nTell me something and i will repeat it back to you\n'
# prompt += "Enter quit to end the program\n"
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)                                #if the message is equal to 'quit', just end the if and while loop



# # Using a flag
# prompt = "Tell me something and I will repeat it for you\n"
# prompt += "Enter quit to end the program\n"
# active = True
# while active:
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
#     else:
#         active = False


# # using break to exit a loop
# prompt = "Please enter the city that you have visited\n"
# prompt += "Please enter 'quit' when you finished\n"

# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"You have visited {city}\n")

# # Using continue in a loop
# current_number = 0
# while current_number <= 10:
#     current_number += 1
#     if current_number%2 == 0:
#         continue
#     print(current_number)

# # exercise 7-5
# age = 0
# prompt = "What is your age? \n"
# prompt += "type 'quit' to quit"
# age = input(prompt)
# age = int(age)
# if