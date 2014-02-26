#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Simple parser for input file.

Assumptions about the input file:

1. Lines that start with a `#` are comment lines and are ignored.
2. Empty lines are ignored.
3. Keywords and data are separated by a colon (:).
4. There is only one keword per line.
5. The keyword `task` is special. It has no data and indicates
   that the next lines will be space seperarted pairs of task
   names and work loads.


"""

import time


def read_tasks(file_name):                                        #1
    """Read task description from text file.
    """

    def convert_date(date_string):                                #2
        """Helper function to convert a string into a date tuple.
        """
        time_tuple = time.strptime(date_string, '%Y-%m-%dT%H:%M') #3
        return time_tuple[:5] # year, month, day, hour, minutes

    converters = {'start_time': convert_date,                     #4
                  'name_of_problem_owner': str,
                  'name_of_programmer': str,
                  'age': int,
                  'skill_level': int}
    fobj = open(file_name)                                        #5
    data = {}                                                     #6
    for line in fobj:                                             #7
        line = line.strip()                                       #8
        if not line or line.startswith('#'):                      #9
            continue
        keyword, entry = [element.strip() for element in          #10
                          line.split(':', 1)]
        if keyword == 'tasks':                                    #11
            break
        else:
            data[keyword] = converters[keyword](entry)            #12
    tasks = []                                                    #13
    for line in fobj:                                             #14
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        task_name, work_load = [element.strip() for element in    #15
                                line.split()]
        tasks.append((task_name, int(work_load)))                 #16
    data['tasks'] = tasks                                         #17
    return data                                                   #18


# self test code
if __name__ == '__main__':
    import pprint                                                 #19
    pprint.pprint(read_tasks('../data/tasks.txt'))                #20
