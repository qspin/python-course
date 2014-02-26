import random
__author__ = 'kristof'

# one, two
value = None
while value != 'end':
    if value is None:
        value = input('Please give your full name:')
        print(value)
    else:
        value = input('Please {} provide your full name again:'.format(value))
        print(value)

# three
def head():
    return 'Number1\tNumber2\tNumber3\n'
def data():
    return ' '.join(map(str, ['{:4d} {:4d} {:4d}\n'.format(random.randrange(0, 1000, 2), random.randrange(0, 1000, 2),
                                         random.randrange(0, 1000, 2)) for x in range(0, 100)]))

print(data())

with open('data_ext12-1.txt', 'w') as file:
    for x in range(100):
        file.write('{:4d} {:4d} {:4d}\n'.format(x, x+10, x+100))

with open('data_ex12-2.txt', 'w') as file:
    file.write(head())
    file.write(data())

# four
with open('data_ext12.txt', 'r') as file:
    res = []
    for line in file:
        res.append([float(x) for x in line.split()])

print(res[:10])