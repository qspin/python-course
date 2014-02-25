__author__ = 'kristof'

# one
def func_print():
    print(' '.join(map(str, range(1, 9))))
func_print()

# two
def func_double(a):
    return a * 2
print(func_double(8))

# three
def func_concat(*args):
    return ' '.join(args) # [x for x in args]
print(func_concat('QSpin', 'python', 'course', 'second', 'day'))

# four
def func_average(a, b, c=None):
    if c is None:
        return float(a + b) / 2
    return float(a + b + c) / 3

print(func_average(12, 19))

def func_averages(*args):
    return float(sum(args)) / len(args)

print(func_averages(12, 19, 33, 54, 11, 25, 25))

# five
print(func_average(33, 21, 18))

# six
def func_measure_time(func, *args, **kwargs):
    import timeit
    start = timeit.default_timer()
    result = func(*args, **kwargs)
    end = timeit.default_timer()
    return result, func.__name__, end - start

print('time to execute', func_measure_time(func_average, 29, 99, 51))
print('time to execute', func_measure_time(func_average, 29, 99, 51))
print('time to execute', func_measure_time(func_average, 29, 99, 51))
print('time to execute', func_measure_time(func_average, 29, 99, 51))
print('time to execute', func_measure_time(func_average, 29, 99, 51))

# refactoring
def check_list(list_, target, m):
    for x in range(0, m):
        target in list_

def check_dict(dict_, target, m):
    for x in range(0, m):
        target in dict_

def check_set(set_, target, m):
    for x in range(0, m):
        target in set_

def main():
    m = 100
    n = int(1e6)
    L = list(range(n))
    target = 'a'
    L[n // 2] = target
    d = dict.fromkeys(L)
    s = set(L)
    measurements = {}

    for func, obj in zip([check_list, check_dict, check_set], [L, d, s]):
        measurements[func.__name__] = func_measure_time(func, obj, target, m)

    time_list = measurements['check_list']
    time_dict = measurements['check_dict']
    time_set = measurements['check_set']

    print('list time', time_list, 'dict time', time_dict, 'ratio dict', time_list[2] / time_dict[2],
          'set time', time_set, 'ratio set', time_list[2] / time_set[2], 'ratio dict_set', time_dict[2] / time_set[2])

if __name__ == '__main__':
    main()