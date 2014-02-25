import timeit

__author__ = 'kristof'

# one
s = set(['kristof', 'jan', 'tom', 'piet', 'hannes'])
s1 = set(['kristof', 'koen', 'patrick', 'peter', 'piet'])

print('kristof' in s)
print('koen' in s)
print('piet' in s1)

print(s.intersection(s1))
print(s & s1)

print(s.union(s1))
print(s | s1)

print(s.difference(s1))
print(s - s1)

# two
s2 = set(['abcd', 'efgh', 'ijkl', 'mnop'])
s3 = set(['abcdefghijklmnopqrst', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrst'])
print(s.issubset(s2))
print(s.issubset(s3))

s4 = s.copy()
s4.add('luc')
print(s.issubset(s4))

print(set(['patrick']).issubset(s1))
print(set(['patrick']) <= s1)

# three
s5 = set(['ellen', 'lien', 'barbara', 'els', 'fien'])
print(s.intersection(s5))

s6 = {frozenset(s), frozenset(s1)}
print(s6)

# four
m = 100
n = int(1e6)
L = range(n)
target = 'a'
L[n // 2] = target
d = dict.fromkeys(L)
s = set(L)

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

start = timeit.default_timer()
for x in range(m):
    target in s
end = timeit.default_timer()
time_set = end - start

print('list time', time_list, 'dict time', time_dict, 'ratio dict', time_list / time_dict,
      'set time', time_set, 'ratio set', time_list / time_set, 'ratio dict_set', time_dict / time_set)