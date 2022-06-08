class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def __add__(self, other):
        if isinstance(other,(int,float)):
            return self.balance+other
        if isinstance(other,BankAccount):
            return self.balance+other.balance
        raise ValueError ('ввести нужно число')
    def __radd__(self, other):
        return self+other
    def __mul__(self, other):
        if isinstance(other,(int,float)):
            return self.balance*other
        if isinstance(other,BankAccount):
            return self.balance*other.balance
        raise ValueError ('ввести нужно число')
a=BankAccount('Иван',300)
b=BankAccount(' Петро', 315)
c=BankAccount('Коля',320)
print(3*c)