#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Read working times from a file.
"""


def read_times(file_name):                                        #1
    """Read input data.

    We assume three columns: weekday   start    end
    The first line is considered a comment.
    The sequence of the columns is important.
    No empty or partial lines are allowed.
    """
    with open(file_name) as fobj:                                 #2
        next(fobj)                                                #3
        data = {}                                                 #4
        for raw_line in fobj:                                     #5
            line = raw_line.split()                               #6
            data[line[0]] = (float(line[1]), float(line[2]))      #7
    return data


# self test code
if __name__ == '__main__':

    def test():                                                   #8
        """Simple test.
        """
        data = read_times(file_name=('../data/times.txt'))
        assert  data == {'Monday': (8.5, 16.0),
                         'Tuesday': (8.5, 16.0),
                         'Thursday': (10.0, 13.0)}

    test()
