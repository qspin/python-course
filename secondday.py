import random
import pickle
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

class Car(object):
    default_colors = ['green', 'black', 'red', 'blue', 'yellow', 'orange', 'white']
    def __init__(self, make, color=None):
        self.make = make
        if not color:
            self.color = random.choice(self.default_colors)
        else:
            self.color = color
        self.mileage = 0
    def go(self, miles):
        self.mileage += miles

car1 = Car('VW', 'black')
print(car1.make)
print(car1.color)
print(car1.mileage)
car1.go(212)
print(car1.mileage)

car2 = Car('Skoda')
print(car2.make)
print(car2.color)

# dictionaries
print(car1.__dict__)
print(Car.__dict__)

class Truck(Car):
    def __init__(self, make, color=None):
        #Car.__init__(self, make, color)
        super(Truck, self).__init__(make, color)
        self.loading = 0
    def go(self, miles):
        self.mileage = miles * 2
    def load(self, loading):
        self.loading += loading

truck1 = Truck('Volvo', 'green')
print(truck1.make)
print(truck1.color)
print(truck1.mileage)
truck1.go(31)
print(truck1.mileage)
print(Truck.mro())

truck2 = Truck('Scania')
print(truck2.make)
print(truck2.color)
print(truck2.loading)
truck2.load(33)
print(truck2.loading)

class CarAdd(Car):
    def __add__(self, other):
        return Car(self.make + other.make, self.color + other.color)

special = add(CarAdd('VW', 'blue'), CarAdd('opel'))
print(special.make)
print(special.color)

class ListAdd(list):
    def __add__(self, other):
        return ListAdd([x + y for x,y in zip(self, other)])

class ListMul(list):
    def __add__(self, other):
        return ListAdd([x * y for x,y in zip(self, other)])

print(ListAdd([1, 2, 3, 4, 5, 6, 7]) + ListAdd([7, 6, 5, 4, 3, 2, 1]))
print(ListMul([1, 2, 3, 4, 5, 6, 7]) + ListMul([7, 6, 5, 4, 3, 2, 1]))

# exceptions
try:
    a = 5
    1 / a.x
except ZeroDivisionError as err:
    print('No Way:', err)
except AttributeError as err:
    print('Huh!', err)

class MyException(Exception):
    pass

try:
    raise MyException('exception has been created')
except MyException as err:
    print('exception has been raised:', err)

# inputs
value = input('Please provide a input value = ')
print(value)

# cmd
# http://docs.python.org/2/library/cmd.html

# argparse
# http://docs.python.org/2/library/argparse.html?highlight=argparse#argparse

file = open('data.txt', 'w')
file.write('line1\nline2\n\nline3')
file.write('\n\nline5\n...')
file.close()

file = open('data.txt', 'r')
print(file.readline())
file.close()

file = open('data.txt')
print(file.read())
file.close()

file = open('data.txt')
print(next(file))
print(next(file))
file.close()

# no need to close the file
with open('data.txt') as obj:
    print(obj)
    print('file is closed:', obj.closed)
    print(next(obj))
print(obj)
print('file is closed:', obj.closed)

p = pickle
d = {'kristof': 'Waardamme', 'els': 'Waardamme', 'Nicole': 'Oostkamp'}
with open('data.pcl', 'wb') as obj:
    p.dump(d, obj)

with open('data.pcl', 'rb') as obj:
    print(p.load(obj))