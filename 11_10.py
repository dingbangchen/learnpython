# Functions
# def great_user():
#     """Display a simple greeting."""
#     print("Hello")
# great_user() #不要忘记括号

# def great_user(username):
#     """Display a simple greeting"""
#     print(f"Hello,{username.title()}")
# great_user('chen')

# # exercise 8-2
# def favorite_book(bookname):
#     print(f"One of my favorite book is {bookname.title()}")
# favorite_book("alice in wonderland")

# # Positional Arguments
# def describe_animal(animal_type,pet_name):
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type} name is {pet_name.title()}")
# describe_animal('hamster', 'harry')
# # Multiple function call
# describe_animal('dog','willie')

# # Keyword Argument
# # A keyword argument is a name_value function pair that you pass to the function
# def describe_animal(animal_type,pet_name):
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type} name is {pet_name.title()}")
# describe_animal(animal_type='hamster',pet_name='harry')
# describe_animal(pet_name='willie',animal_type='dog')



# # Default Values
# def describe_animal(pet_name,animal_type='dog' ):
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type} name is {pet_name.title()}")
# describe_animal(pet_name='willie')
# describe_animal('willie2')
# describe_animal('harry','hamster')  #If we still have two input for the function, it will still override it

# # exercise 8-3
# def make_tshirt(size,text):
#     print(f"This tshirt is size {size.upper()}, and it prints {text}")
# make_tshirt('M','blablabla')
# make_tshirt('s',text='jfoiajoiwnve')

# # exercise 8-4
# def make_tshirt(size = 'L',text = 'I love Python'):
#     print(f"This tshirt is size {size.upper()}, and it prints {text}")
# make_tshirt()
# make_tshirt('M')
# make_tshirt('S','I love C')



# Returning Value
# # Return a simple value
# def get_formatted_name(first_name,last_name):
#     """Return a full name,neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi','hendrix')
# print(musician)

# Making an argument optional
def get_formatted_name(first_name, last_name,middle_name =''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician1 = get_formatted_name('john','lee','hooker')
musician2 = get_formatted_name('jimi','hendrix')
print(musician1)
print(musician2)