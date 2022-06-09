class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 1 <= item <= len(self.values):
            return self.values[item]
        else:
            raise IndexError('нет такого индекса')

    def __setitem__(self, key, value):
        if 1 <= key <= len(self.values):
            self.values[key] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([None] * diff)
            self.values[key-1] = value
        else:
            raise IndexError('не понятный индекс')

    def __delitem__(self, key):
        if 0 <= key <= len(self.values):
            del self.values[key]
        else:
            raise IndexError('НЕТ ИНДЕКСА')


a = Vector(5,4,7,8,9,15,54)
print(a)
print(a[3])
a[12]=10
print(a)
a[8]='создатель Яхия'
print(a)
del a[10]
print(a)