class Student:

    @staticmethod
    def is_full_name(name : str):

        namesplit = name.split(" ")

        return len(namesplit) > 1

    


if __name__ == "__main__":

    print(Student.is_full_name("John Smith"))
    print(Student.is_full_name("John"))

    student = Student()

    print(student)