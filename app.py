class Student:
    def __init__(self, name):
        self.name= name
    def greeting(self):
        f'Hello, my name is {self.name}'
    def reason(self):
        f'I have always wanted to learn coding'

class Instructor(Student):
    def __init__(self, name):
        super().__init__(name)
    



