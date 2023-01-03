# Generators

# Eager Loading

def generate_square(n):
    return [ i**2 for i in range(1,n) ]

for x in generate_square(100):
    print(x)

# Lazy Loading

def generate_squares(n):
    for i in range(1,n):
        yield i**2

it = iter(generate_squares(10))
next(it)

for i in generate_squares(10):
    print(i)

# Keyword:-- Yield

from time import sleep

def func():
    print("started")
    yield
    sleep(5)
    print("ended")

print("hello")
it = iter(func())
next(it)
print("world")
next(it)



def func():
    print("start")
    yield 1
    print("yielded 1")
    yield 2
    print("yielded 2")

it = iter(func())
next(it)

a = ( i**2 for i in range(10))
for i in a:
    print(i)

a = ( i**2 for i in range(10) )
print(iter(a))