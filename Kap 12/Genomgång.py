__author__ = 'ab53995'

class Address():
    def __init__(self):
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""

# Create an address
home_address = Address()

# Set the fields in the address
home_address.name = "John Smith"
home_address.line1 = "701 N. C Street"
home_address.line2 = "Carver Science Building"
home_address.city = "Indianola"
home_address.state = "IA"
home_address.zip = "50125"

# Create another address
vacation_home_address = Address()

# Set the fields in the address
vacation_home_address.name = "John Smith"
vacation_home_address.line1 = "1122 Main Street"
vacation_home_address.line2 = ""
vacation_home_address.city = "Panama City Beach"
vacation_home_address.state = "FL"
vacation_home_address.zip = "32407"

def print_address(address):
    print(address.name)
    # If there is a line1 in the address, print it
    if len(address.line1) > 0:
        print(address.line1)
    # If there is a line2 in the address, print it
    if len(address.line2) > 0:
        print( address.line2 )
    print(address.city + ", " + address.state + " " + address.zip)


class Cat():
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = ""

    def meow(self):
        print("Meow")

my_cat = Cat()
Cat.name = "Bruce"
Cat.color = "Brown"
Cat.weight = "20 pounds"
#my_cat.meow()


class Monster():
    def __init__(self, new_name,new_health ):
        self.name = new_name
        self.health = new_health

    def decrease_health(self):
        self.health -= self.amount
        if self.health < 1:
            print("The animal died.")

class Dog():
    def __init__(self):
        # Constructor. Called when creating an object of this type.
        self.name = ""
        print("A new dog is born!")

# This creates the dog
# my_dog = Dog()


class Star():
    def __init__(self):
        print("A new star is born!")

kurt = Monster("Kurt", 200)
