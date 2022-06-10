class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]

    def __iter__(self):
        return iter(self.surname)

a = Student('Иван', 'Иванов', [4, 4, 5, 4, 5])
for i in a:
    print(i)
