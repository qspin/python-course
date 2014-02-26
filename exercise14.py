import programmersworld
from programmersworld import world as w
import inspect
__author__ = 'kristof'

# one
a = 3
b = 3

print(a == b)
print(a is b)
print('a id', id(a), 'b id', id(b))
print('a type', type(a), 'b type', type(b))

a = 3
b = 3.0

print(a == b)
print(a is b)
print('a id', id(a), 'b id', id(b))
print('a type', type(a), 'b type', type(b))

a = 'hello'
b = 'Hello'
c = 'hello'

print(a == b)
print(a == c)
print(a is b)
print(a is c)
print('a id', id(a), 'b id', id(b), 'c id', id(c))
print('a type', type(a), 'b type', type(b), 'c type', type(c))

# two
print(dir(programmersworld))
# print(inspect.getmembers(programmersworld))

print(w.os)
print(dir(w))