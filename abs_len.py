class Person:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def __len__(self):
        return abs(self)
    def __abs__(self):
        return abs(self.x2-self.x1)


a = Person(10, 5)
print(len(a))