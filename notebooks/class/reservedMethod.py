"""
__init__
__str__
__dict__
"""

class Temp:

    def __init__(self):
        self.lut = {}
        print("constructor")

    def __str__(self):
        """Returns the string representation of the object"""
        return "Temp Class"


if __name__ == "__main__":

    a = Temp()

    print(a.__str__())

    print(a.__dict__)