# Passing a list
# # greet_user.py
# def greet_users(names):
#     """Create simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)
# usernames = ['hannah','ty','margot']
# greet_users(usernames)

# # Modifying a list in a function
# unprinted_design=['phone case','robot pendant','dodecahedron']
# printed_design=[]

# while unprinted_design:
#     current_design = unprinted_design.pop()
#     print(current_design)
#     printed_design.append(current_design)

# for designs in printed_design:
#     print(designs)

# if we do this in functions:
def print_models(unprinted_models,printed_models):
    while unprinted_models:
        current_design = unprinted_models.pop()
        # print(current_design)
        printed_models.append(current_design)
def show_printed_models(printed_models):
    for printed_model in printed_models:
        print(printed_model)

unprinted_models = ['phone case','robot pendant','dodecahedron']     #这里就相当于把之前的key argument 放到外面来了
printed_models=[]
print_models(unprinted_models,printed_models)
show_printed_models(printed_models)