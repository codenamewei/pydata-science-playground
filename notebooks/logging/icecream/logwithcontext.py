from icecream import ic
ic.configureOutput(includeContext=True)

def foo():
    ic('str')

foo()