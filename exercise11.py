__author__ = 'kristof'

# one, two, three
try:
    xyz
    print('Done!')
except NameError as err:
    print('Error has occurred:', err)
    print('Done!')

# four
l = list(range(5))
try:
    l[7] * 2
except IndexError as err:
    print('List index doen\'t exist:', err)

# five
def my_get(dict, key, default=None):
    try:
        return dict[key]
    except KeyError as err:
        print('key not found:', err)
        return default

d = {'kristof': 'Waardamme', 'els': 'Waardamme', 'Nicole': 'Oostkamp'}
print('kristof\'s location', my_get(d, 'kristof', 'Oostkamp'))
print('hugo\'s location', my_get(d, 'hugo', 'Oostende'))

# six
class PositiveOnly(Exception):
    pass

try:
    a = -5
    if a < 0:
        raise PositiveOnly('found {} but need positive value'.format(a))
except PositiveOnly as err:
    print('number not correct:', err)