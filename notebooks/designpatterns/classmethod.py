#without @classmethod
class StudentOri:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

#basic @classmethod
class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, strname):
        first_name, second_name = map(str, strname.split(" "))
        student = cls(first_name, second_name)
        return student

#static factory method to encapsulate object creation
class StudentFactory:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    @classmethod
    def from_string(cls, strname):
        first_name, second_name = map(str, strname.split(" "))
        student = cls(first_name, second_name)
        return student

    @classmethod
    def from_json(cls, json_obj):
        #parse json
        student = cls("Json First", "Json Last")
        return student

    @classmethod
    def from_pickle(cls, pickle_file):
        #load pickle file...
        student = cls("Pickle first", "Pickle Last")
        return student

    def __str__(self):

        return f"{self.first_name} {self.last_name}"


scott1 = StudentOri('Scott',  'Robinson')

scott2 = Student.from_string('Scott Robinson')

print(StudentFactory.from_string("Lion King"))
print(StudentFactory.from_json(None))
print(StudentFactory.from_pickle(None))
