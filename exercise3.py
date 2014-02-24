__author__ = 'kristof'

tuple = (12, 33, 17, 23.9, 14.11, '333', 'test', 'aha')
sub_tuple = tuple[2:-2]

print("sub tuple ", sub_tuple)

print(tuple*3)
print(tuple+tuple+tuple)

print("reverse: ", sub_tuple[::-1])
print("reverse every 2: ", sub_tuple[::-2])

print('a' in tuple)
print('aha' in tuple)