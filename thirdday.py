import datetime as dt
import sys
import os
import shutil
import subprocess

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

a = 10

def func():
    a = 100
    print('in', a)
    print(locals())

print('before', a)
func()
print('after', a)

def func2():
    global a  # global usage => python2 and python3
    a = 100
    print('in', a)
    print(locals())

print('before', a)
func2()
print('after', a)

def func3():
    a = 10
    def inner():
        nonlocal a  # nonlocal will use only the variable from the scope just above it => only python3
        a = 100
        print('in', a)
    print('before', a)
    inner()
    print('after', a)

func3()

print(globals())

def outer(arg):
    def inner(inner_arg):
        return arg + inner_arg
    return inner(10)

print(outer(5))

def outer2(arg):
    def inner(inner_arg):
        return arg + inner_arg
    return inner

print(outer2(5)(10))

print(sys.version)
print(sys.version_info)
print(len(sys.__dict__))

s = 'hello world'
print(s.capitalize())
print(s.upper())
print(s.center(40, "#"))
print(s.count('l'))
print('_'.join(s))

print('%04d' % 44)
print('%04d %7.3f %d' % (3, 45.6, 44))
print('%(v1)04d %(v2)7.3f %(v1)d' % {'v1': 3, 'v2': 45.6})
print('{0:04d} {1:f} {v1}'.format(31, 36.76, v1=121))
print('{0:04d} {1:f} {v1}'.format(31, 36.76, **{'v1': 141}))

print('sys.executable', sys.executable)
print('sys.getcheckinterval', sys.getcheckinterval())
print('sys.getdefaultencoding', sys.getdefaultencoding())
print('sys.getfilesystemencoding', sys.getfilesystemencoding())
print('sys.getrecursionlimit', sys.getrecursionlimit())
print('sys.maxsize', sys.maxsize)
print('sys.maxunicode', sys.maxunicode)

print('os.getcwd', os.getcwd())
print('os.getpid', os.getpid())
print('alternative seperator', os.path.altsep)

help(os.walk)
help(shutil.move)

subprocess.call(['ls', '-al'])
print('printed to file: ls_output.txt', subprocess.check_output(['ls', '-al']))
file = open('ls_output.txt', 'wb')
file.write(subprocess.check_output(['ls', '-al']))
file.close()
# with open('ls_output.txt', 'w') as obj:
#     obj.write(str(subprocess.check_output(['ls', '-al'])))
