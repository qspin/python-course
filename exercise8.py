import os
__author__ = 'kristof'

# one
print(' '.join(map(str, (x * 3 for x in range(21)))))

# two
def even(x):
    return not x % 2

print(' '.join(map(str, filter(even, (x * 3 for x in range(0, 21))))))
print(' '.join(map(str, (x * 3 for x in range(21) if x * 3 % 2 == 0))))

# three
print(' '.join(map(str, (10, 100, 200, 300, 400, 500, 600, 700, 800, 900))))
print(' '.join(map(str, (x * 100 for x in range(1, 10)))))

def generator():
    yield 10
    for x in range(100, 901, 100):
        yield x
print(' '.join(map(str, list(generator()))))

# four
#  Python process   4,1 MB
print(os.getpid())

n = int(1e3)
[x * x for x in range(n)]

input()

print(os.getpid())