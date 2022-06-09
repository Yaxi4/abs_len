class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __len__(self):
        return abs(self.x-self.y)
    def __bool__(self):
        return self.x!=0 or self.y!=0
print(bool(Point(2,3)))
print(bool(Point(5,5)))
print(bool(Point(0,3)))
print(bool(Point(2,0)))
print(bool(Point(0,0)))
print(len(Point(5,6)))