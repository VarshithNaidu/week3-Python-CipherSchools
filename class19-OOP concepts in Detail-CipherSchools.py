# The __init__ method

a = 5

def func():
    pass

print(type(func))

print(isinstance(func, object))

class A:
    name = "jathin"
    marks = 50

print(type(A))
print(type(object))
print(type(int))

class A:
    def __call__(self):
        print("You called me")

a = A()
print(type(a))
print(a())

b = A.__call__(A)

a = {"name": "jathin"}
print(a["name"])
print(a.__getitem__("name"))

class Exponent:
    def __init__(self,n):
        self.n = n

    def __getitem__(self,x):
        return x ** self.n

e = Exponent(3)
print(e[6])

class A:
    name = "jathin"
    def __init__(self,n):
        self.n = n

a = A(2)
print(a.name)
print(a.n)

class Dog:

    tricks = []
    def __init__(self,name):
        self.name = name

    def add_trick(self,trick):
        self.tricks.append(trick)

d1 = Dog("Maxx")
d1.add_trick("fetch")
d1.add_trick("talk")
print(d1.tricks)

d2 = Dog("Bella")
d2.tricks
