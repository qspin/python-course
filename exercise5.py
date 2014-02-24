import timeit

__author__ = 'kristof'

# one
d = {'name 1': '0479222222', 'name 2': '0479333333', 'name 3': '0479444444', 'name 4': '0479555555'}
print(d)

print 'Telephone number for name 3 is ', d['name 3']

del d['name 2']
print(d)

print(d.keys())
print(d.values())

for x in d:
    print(x)

for x in d:
    print(d[x])

for x, y in d.items():
    print 'Phone number for', x, 'is', y

# two
print(d.get('lisa'))
print(d.get('lisa') is None)
print(d.get('name 6', 1))
d.setdefault('name 7', 0)
print(d['name 7'])

# three
d2 = {'name 5': '0479666666', 'name 6': '0479777777', 'name 7': '0479888888', 'name 8': '0479999999'}

for x, y in d2.items():
    d[x] = y
print(d)

d.update(d2)
print(d)

# four
del d['name 8']
print(d)

print(d.pop('name 6'))

print(d.popitem())

# five
m = 100
n = int(1e6)
L = range(n)
target = 'a'
L[n // 2] = target
d = dict.fromkeys(L)

start = timeit.default_timer()
for x in range(m):
    target in L
end = timeit.default_timer()
time_list = end - start

start = timeit.default_timer()
for x in range(m):
    target in d
end = timeit.default_timer()
time_dict = end - start

print(time_list, time_dict, time_list / time_dict)