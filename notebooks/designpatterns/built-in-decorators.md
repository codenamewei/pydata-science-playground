Built in decorators are just **syntactic sugar**.  
The following two definitions create equal functions 
```
def f(...):
    ...
f = staticmethod(f)

@staticmethod
def f(...):
```

### Static Method

- A static method is a method that belongs to a class rather than an instance of a class.
- To contain logic pertaining to the class, but that logic should not have any need for specific class instance data.
- [Decorator @staticmethod](staticmethod.py)

### Class Method 
- is useful when you make that class as a factory
- [static factory pattern](https://stackoverflow.com/questions/929021/what-are-static-factory-methods/929273#929273)
- [Decorator @classmethod](classmethod.py)
