from time import perf_counter


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'запустили функцию {self.func.__name__}')
        result = self.func(*args, **kwargs)
        finish = perf_counter()
        print(f' функция {self.func.__name__} отработала за {finish - start}')
        return result

#@Timer
def factorial(n):
    pr = 1
    for i in range(1,n+1):
        pr *= i
    return pr

def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
factorial=Timer(factorial) #можно заменить декоратором @Timer над функций factorial
print(factorial(3))
Timer(fib)(10)             #fib не стоит декарировать. Декорируем только вызов конечного результата
print(fib(3))