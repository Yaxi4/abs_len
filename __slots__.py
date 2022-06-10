from timeit import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    #__slots__ = (x, y)

    def __init__(self,x,y):
        self.x = x
        self.y = y
def make_1():
    s=Point(3,4)
    s.x=100

    del s.x
def make_2():
    s=PointSlots(3,4)
    s.x=100

    del s.x
print(timeit(make_1))
print(timeit(make_2))