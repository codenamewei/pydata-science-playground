from icecream import ic


def first():
    pass

def second():
    pass

def third():
    pass

def foo():
    ic()
    first()

    if True:
        ic()
        second()
    else:
        ic()
        third()


if __name__ == "__main__":
    ic("Hello world")
    ic()
    foo()