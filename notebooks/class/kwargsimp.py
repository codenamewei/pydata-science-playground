

def testkwargs(var1, **kwargs):

    """
    Why use **kwargs
    - to pass unspecified number of arguments to a function 

    both *args and **kwargs are just conventions
    - *args: for non-keyworded variable length argument
    - **kwargs: for keyworded variable length argument 

    The important thing is the asterisk * and **. 
    The name is just convention.

    Use case: 
    - to make function decorator
    - monkey patching (modifying code during runtime)
    """

    print(var1)

    print("Key: ")
    print(kwargs.keys())
    print("Values: ")
    print(kwargs.values())

def testargs(*args):

    print([i for i in args])


print("*****************testkwargs*****************")
testkwargs("123", a = "123", b = "456", c = "789")

print("*****************testargs*****************")
testargs(123,456)