def func(a,b):
    print(a,b)

def func():
    print("wait")

class A:
    def __init__(self):
        print("A init executed")

class B(A):
    def __init__(self):
        print("B init executed")
        super().__init__()

abc = B()

# MRO(METHOD RESOLUTION ORDER)

class A:
    x = 5

class B(A):
    pass

class C(B):
    pass

class D(A):
    x = 10

class E(C,D):
    pass

e = E()
print(e.x)

print(E.mro())

# DFS
# if there is a loop branch solve differently

# Iteration Protocol

a = range(5)
it = a.__iter__()
print(it)

class myrange:
    def __init__(self,n):
        not self

    def __iter__(self):
        pass

a = [1, 2, 3, 4]
print(iter(a))

class myrange:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        return myrange_iterator(self)

class myrange_iterator:
    def __init__(self, myrange):
        self.myrange = myrange
        self.i = 0

    def __next__(self):
        ret = self.i
        self.i += 1

        if ret >= self.myrange.n:
            raise StopIteration

        return ret

for i in range(5):
    print(i)

a = myrange(5)
it = iter(a)
print(next(it))

