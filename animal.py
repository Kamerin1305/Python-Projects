"""
'animal.py' is a program that prints out the type of Lion based
on it's weight. The main objective of this program is to teach the coder
on class and class inheritance. It utilises on Super Class and
on Inherited Class.
"""


class Animal():
    """
    Animal class docstring.
    This is the Super Class that receives the following variables:
        a. numteeth
        b. spots
        c. weight
    """

    # call the class constructor and initiate the variables
    def __init__(self, numteeth, spots, weight):
        self.numteeth = numteeth
        self.spots = spots
        self.weight = weight


# create the inherited class with the Super Class called in the parenthesis
class Lion(Animal):
    """
    Lion class string.
    This is the Inherited class that inherits from the Animal class
    It also adds a field called colour
    """
    # call the class constructor again to initiate the new field and receive
    # the inherited class attributes

    def __init__(self, colour, numteeth, spots, weight):
        super().__init__(numteeth, spots, weight)
        self.colour = colour

    def type_lion(self):
        """this function test whether a lion
        based on the weight field is a
            a. cub - less than 80KG's
            b. female - less than 120 KG's
            c. male - more than 120 KG's
        """
        # set the conditional statements for the needed outcomes
        # based on the parameters given
        if self.weight < 80:
            print("this is a cub")
        elif self.weight < 120:
            print("this is a female")
        elif self.weight > 120:
            print("this is a male")


class Cheetah(Animal):
    """
    Cheetah class string.
    This is the Inherited class that inherits from the Animal class
    It also adds a field called unique
    """
    # unique = ["Fastest land animal", "Non-retractable claws"] -
    # I can utilise a class constant array without initiating it
    # in the constructor and then call an empty [] in the object created.
    # call the class constructor again to initiate the new field and receive
    # the inherited class attributes.

    def __init__(self, unique, numteeth, spots, weight):
        super().__init__(numteeth, spots, weight)
        # unique is a variable set and receives an array list of two unique chars of cheetas
        self.unique = unique

    def print_object(self):
        """this function prints the cheetah object created and thrown into it"""
        print(f"\nUnique factors of a Cheetahs are:")
        for i in self.unique:  # for loop for printing the unique field array
            print(i)
        print(f"\nThey have {str(self.numteeth)} teeth\n")
        print(
            f"Do they have spots? {str(self.spots)}\n\nThey weigh around {str(self.weight)}")


# declare three lions by creating three lion objects
# fields must now include the extra colour field
LION1 = Lion("Golden Yellow", 15, "No", 70)
LION2 = Lion("Golden Yellow", 30, "No", 95)
LION3 = Lion("Golden Yellow", 30, "No", 130)


# run the methods to print the type of lion
LION1.type_lion()
LION2.type_lion()
LION3.type_lion()
# create a cheetah object with the array
CHEETAH1 = Cheetah(
    ["Fastest land animal", "Non-retractable claws"], 50, "Yes", "95")
# call the method to print the object
CHEETAH1.print_object()
