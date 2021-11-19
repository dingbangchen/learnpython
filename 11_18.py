# # Creating a Dog class
# class Dog:
#     """A Simple attempt to model a dog"""
#     def __init__(self,name,age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         """Simulate a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting")

#     def roll_over(self):
#         """Simulate roll over in response to a command"""
#         print(f"{self.name} is rolling over!")

# # Making an instance from a class
# my_dog = Dog('Willie',6)

# print(f"my dog's name is {my_dog.name}")
# print(f"it is {my_dog.age}-years old")
# my_dog.sit()
# my_dog.roll_over()

# # We can create as many instances as we want
# your_dog = Dog('Lucy',3)
# print(f"Your dog's name is {your_dog.name}")
# print(f"Your dog is {your_dog.age}-years old")
# your_dog.sit()



# # exercise 9-1
# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name = restaurant_name
#         self.type = cuisine_type
#     def describe_restaurant(self):
#         print(f"{self.name} has {self.type}")
#     def open_restaurant(self):                                   #注意这里的self不能少，需要从class传入一个local variabel
#         print(f"The {self.name} is now opening")

# restaurant1 = Restaurant('restaurant 1', 'Chinese food')
# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()


# # exercise 9-3
# class User:
#     def __init__(self,first_name,last_name,gender,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.gender = gender
#         self.age = age
#     def describe_user(self):
#         print(f"User name {self.first_name} {self.last_name} is {self.gender} and {self.age}-years old")
#     def greetUser(self):
#         print(f"Hi,{self.first_name} {self.last_name}")

# user1 = User('Dingbang','Chen','male',23)
# user1.describe_user()
# user1.greetUser()


# # Working with classes and instances
# class Cars:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_describe_name(self):
#         """Return a neatly formatted descriptive name"""
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
# my_new_car = Cars('audi','q5',2012)
# print(my_new_car.get_describe_name())



#Setting a Default value for an attribute
# Working with classes and instances
class Cars:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0          #let's add a new attribute with assigned default value
   
    def get_describe_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    # Modifying an attribute's value through a method
    def update_odometer(self,milage):
        """Set the odometer reading to the given value"""
        self.odometer_reading = milage
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can not roll back an odometer!")

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    #And new function for the odometer
    def read_odometer(self):
        """print a statement showing the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it")



my_new_car = Cars('audi','q5',2012)
print(my_new_car.get_describe_name())
my_new_car.read_odometer()       # Call this function

# modifying an attribute's value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(24)
my_new_car.read_odometer()

my_used_car = Cars('subaru','outback',2015)
print(my_used_car.get_describe_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(500)
my_used_car.read_odometer()