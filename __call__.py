class Counter:
    def __init__(self):
        self.count = 0
        self.summa = 0
        self.lengh = 0
        self.srednee = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        self.summa += sum(args)
        self.lengh += len(args)
        self.srednee += self.summa / self.lengh
        print(f'наш {self.__name__} вызывался {self.count} раз')
        print(self.summa, 'ghbdt')

b=Counter()
b(100,200,300)
print('-----------------')

a=Counter()
a(4,5)
print(a.summa)
print(a.lengh)
print(a.srednee)
print('-----------------')
