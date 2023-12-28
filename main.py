from datetime import datetime
from functools import wraps

# ex1
def MyDecorator(func):
    def wraper(*args, **kwargs):
        before = datetime.now()
        func(*args, **kwargs)
        after = datetime.now()
        print(after - before)
    return wraper

@MyDecorator
def myprint():
    for i in range(1000):
        print(i)

# myprint()

# ex2
cache = {}

def Decoratorcache(func):
    @wraps(func)
    def wraper(*args, **kwargs):
        print(args[0])
        if args[0] in cache:
            return cache[args[0]]
        else:
            result = func(*args, **kwargs)
            cache.update({args[0]:result})
            print(result)
            return result
    return wraper

@MyDecorator
@Decoratorcache
def fib(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x


@MyDecorator
def fib1(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

fib(10000)
fib(12000)
fib1(10000)
fib1(20000)
print(cache)


