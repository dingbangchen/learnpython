# # send a copy of a list to a function:
# function_name(list_name[:])

# # exercise 8-9
# def show_messages(messages):
#     for message in messages:
#         print(message.title())
# list_message = ['hello','my name is ','dingbang']
# show_messages(list_message)



# # Passing a arbitrary number of arguments
# def make_pizza(*toppings):
#     # """Print the list of toppings that have been requested"""
#     # print(toppings)
#     """Summarize the pizza that we are about to make"""
#     print("Making a pizza with following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")
# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')


# # Mixing positional and arbitrary arguments
# # Python matches positional and keyword arguments first and then collect any remaining arguments in the final parameter
# def make_pizza(size,*toppings):
#     """summarize the pizza we are about to make"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green_peppers','extra cheese')


# Using arbitrary keyword argument
def build_profile(first,last,**user_info):
    """Build a dictionary containing everything we know about a user"""
    print(user_info)
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')
print(user_profile)   