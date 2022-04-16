import random 

class CourseBook:

    def __init__(self, course = None):

        self._counter = course

    def getcourse(self):

        return self._counter()

class Calculus:

    def __str__(self):

        return "Calculus"


    def getinfo(self,):

        return "Calculus info"


class Algorithm:

    def __str__(self):

        return "Algorithm"

    def getinfo(self):

        return  "Algorithm info"


class Management:

    def __str__(self):

        return "Management"

    def getinfo(self):

        return "Management info"

def random_course():

    return random.choice([Calculus, Algorithm, Management])

if __name__ == "__main__":

    for i in range(0,5):
        coursebook = CourseBook(random_course())
        course = coursebook.getcourse()
        print(course.getinfo())

