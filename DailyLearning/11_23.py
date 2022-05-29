# # electric_car.py which inherit from car.py

# class Car:
#     """A simple attempt to represent a car"""

#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")

#     def update_odometer(self,milage):
#         if milage >= self.odometer_reading:
#             self.odometer_reading = milage
#         else:
#             print("you can not roll back an odometer!")
    
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles

# class ElectricaCar(Car):                             # The name of parent class must be included in parenthese in child class
#     """Represent aspects of a car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year)

# my_tesla = ElectricaCar('tesla','model s',2019)
# print(my_tesla.get_descriptive_name())
# #  when you create a child class, the paren class must be part of the current file 
# # and must appear before the child class in the file




# # Defining attribute and methods for the child class
# # electric_car.py which inherit from car.py

# class Car:
#     """A simple attempt to represent a car"""

#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")

#     def update_odometer(self,milage):
#         if milage >= self.odometer_reading:
#             self.odometer_reading = milage
#         else:
#             print("you can not roll back an odometer!")
    
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles

# class ElectricaCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attribute specifc to an electric car
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 75
    
#     def get_describe_battery(self):
#         print(f"the car has a {self.battery_size}-kWh battery.")

# my_tesla = ElectricaCar('tesla','model s',2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.get_describe_battery()




# Instances as attributes
class Car:
    """A simple attempt to represent a car"""

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self,milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("you can not roll back an odometer!")
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self,battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
class ElectricaCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attribute specifc to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()
  
my_tesla = ElectricaCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()





# Importing Classes 详见书第174页起