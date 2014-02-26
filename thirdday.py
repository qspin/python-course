import datetime as dt
import sys

__author__ = 'kristof'

day = dt.datetime.today()
print(day)

day2 = dt.datetime(2014, 2, 25, 10, 5, 30)
print(day2)

print('difference between the days:', day - day2)

dayAdd = dt.timedelta(10)
print('add 10 days:', day + dayAdd)

# imports
#import sys
#from sys import argv
#from sys import argv as arg

print(sys.path)
# ['/Users/kristof/Work/python',
#  '/Library/Frameworks/Python.framework/Versions/3.3/lib/python33.zip',
#  '/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3',
#  '/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/plat-darwin',
#  '/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/lib-dynload',
#  '/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/site-packages']

L1 = [1, 2, 3]
L2 = [1, 2, 3]
L3 = L2

print(L1 == L2)
print(L1 is L2)
print(L2 == L3)
print(L2 is L3)
print('id L2', id(L2), 'id L3', id(L3))
L3[0] = 4
print(L2 == L3)
print(L2 is L3)
L3 = 5
print(L2 == L3)
print(L2 is L3)


i1 = 2000
i2 = 2000

print(i1 == i2)
print(i1 is i2)
i1 = i2
print(i1 == i2)
print(i1 is i2)

print(str('a'))
print(repr('a'))
print(eval(repr('a')))

# dynamic attributes
class A(object):
    def __init__(self, attr1, attr2='attributes'):
        self.attr1 = attr1
        self.attr2 = attr2

a = A('attribute')
print(a.attr1)
print(getattr(a, 'attr1'))
print(getattr(a, 'attr2'))

for x in dir(a):
    if not x.startswith('__'):
        print(x, getattr(a, x))

# unicode characters are allowed in python3
ä = 34
print('ä value id', ä)


# keywords
def keywords():
    import keyword as k
    print(k.kwlist)

keywords()