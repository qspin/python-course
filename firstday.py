# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import copy

__author__ = 'kristof'

s = """line1
line2

line4"""

print(1 + 1)

print('Kristof', u'Ryheül')

print(s)

print(10 if 1 < 2 else 100)

value = raw_input('Enter: ')

print("{0}".format(value))

range(11, 2, -1)

for x in range(11):
    print(x, end=' ')

print(sys.float_info)
print('\n\n')
print(sys.maxint)

s = 'abcdefg'

'abc' in s

'ac' not in s

# reverse order
s[::-1]

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L[2:4] = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print(L)

s = 'AXaxYgAy'
print(sorted(s, key=str.lower))
print(s)

lt = [(1, 2, 4), (2, 4, 8), (2, 4, 1)]
def function(f): return f[1] >= 4
print(filter(function, lt))
print(lt)

L = [x * x for x in range(2, 11)]
print(L)

d = {10: 'x', 'a': 100, 'b': [1, 2, 3], (1, 2, 3): 123456}
print(d)
d['c'] = 43
print(d)

#shallow copy
d2 = d.copy()
d2[10] = 'xxx'
print(d, d2)

d2['b'][0] = 22
print(d, d2)

#deep copy
d3 = copy.deepcopy(d)
d3['b'][1] = 66
print(d, d2, d3)

d.update({'a': -14, 'd': 'insert'})
print(d)

d = dict(zip('abcde', (9, 8, 7, 6, 5)))
print(d)