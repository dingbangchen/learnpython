# Storing your functions in Modules
#  代码实现过于复杂，详看书第150页起


# Classes 
# Creating a Dog class
class Dog:
    """A Simple attempt to model a dog"""
    def __init__(self,name,age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate roll over in response to a command"""
        print(f"{self.name} is rolling over!")