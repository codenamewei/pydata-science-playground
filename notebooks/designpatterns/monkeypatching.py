

class Temp:

    def testfunc(self):

        print("hello")


def testfunc(self):

    a = 100

    print(a + 100)

if __name__ == "__main__":

    temp1 = Temp()

    temp1.testfunc()

    #monkey patching
    Temp.testfunc = testfunc

    temp2 = Temp()

    temp2.testfunc()