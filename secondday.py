__author__ = 'kristof'

s = set([1, 2, 3, 1, 2, 2, 1, 3, 4, 2, 4, 1, 2])
s1 = set([3, 5, 4, 8, 9, 8, 4, 5, 6, 7])

print(s)
print(s.intersection(s1))
print(s & s1)
print(s1 - s)
print(s.union(s1))
print(s | s1)

s.pop()
print(s)

# print all the functions related to the set
sm = set([x for x in dir(s) if not x.startswith('__')])
print(sm)

fz = frozenset((3, 4, 5, 6))
fzm = set([x for x in dir(fz) if not x.startswith('__')])
print(fzm)

print(sm - fzm)

def add(a, b=0):
    return a + b

print(add(1, 2))
print(add(4.5, 3))
print(add([1, 2, 3], [3, 4, 5]))
print(add(7))
print(add(b=12, a=3))

# undefined number of arguments
def func1(*args):
    return args

# keyword arguments
def func2(**kwargs):
    return kwargs

def call_func(func, *args, **kwargs):
    print('calling')
    return func(*args, **kwargs)

print(func1(1, 2, 5, 4))
print(func2(a=1, b=2, c=3))
print(call_func(add, 3, 4))

def func3():
    return 1, 2, 3

print(func3())
a, *b = func3()
print('a =', a, 'b =', b)
print(id(a))

# generators & iterators
def simple():
    print('start')
    yield 1
    print('after 1')
    yield 2
    print('after 2')
    yield 3
    print('end')

s = simple()
for x in range(0, 3):
    next(s)

def endless(start=0):
    value = start
    while True:
        yield value
        value += 1

e = endless()
for x in range(0, 100):
    print(next(e), end=' ')
print('\n')