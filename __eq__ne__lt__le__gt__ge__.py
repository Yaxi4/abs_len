class Rectancle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectancle):
            return self.a == other.a or self.b == other.b

    def __lt__(self, other):
        if isinstance(other, Rectancle):
            return self.area < other.area
        if isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other

a=Rectancle(5,10)
b=Rectancle(7,11)
print(a==b)
print(a>b)
print(a<b)
print(a==50)