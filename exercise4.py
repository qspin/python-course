import timeit

__author__ = 'kristof'

# one
L = range(0, 20)
print(L)
L[0] = 33
print(L)

# two
# del L[2]
L[2:6] = range(19, 27)
print(L)

# three
L.extend((61, 62, 63, 64, 65))
print(L)

# four
L.pop()
print(L)

# L[-1:] = []
L = L[0:-1]
print(L)

L.pop(len(L)-1)
print(L)

# five
L[::-1]
print(L)

# six
L1 = [1, 2, 3, 4, 5]
print(L1)
L2 = ['a', 'b', 'c', 'd', 'e']
print(L2)
print(zip(L1, L2))

# seven
L = []
for x in L1:
    L.append(x*10)
print(L)

L = [x * 10 for x in L]
print(L)

# eight
L = [3, 2, 9, 4, 10, 3, 2, 9, 8, 5, 6, 11, 23, 22, 41, 11, 1, 3, 9, 20, 8, 7, 17, 6]
print(L)

def even(x):
    return x % 2

def even2(x):
    return x % 2, x

print(sorted(L, key=even))
print(sorted(sorted(L), key=even))
print(sorted(L, key=even2))

# nine
times = [pow(10, x) for x in range(5, 8)]
print(times)
L = []
s = ''

for x in times:
    start = timeit.default_timer()
    for y in range(x):
        s += 'a'
    end = timeit.default_timer()
    time_a = end - start
    print('time a: ', time_a)
    start = timeit.default_timer()
    for y in range(x):
        L.append('a')
    s2 = ''.join(L)
    end = timeit.default_timer()
    time_b = end - start
    print('time b: ', time_b)
    print(s == s2)
    print 'ratio', time_a / time_b
