# -*- coding: utf-8 -*-

"""
Module with classes Programmer and Task.

A Programmer solves a problem by developing
a computer program.
Task contains the problem to be solved.
"""

from __future__ import print_function, unicode_literals

import pickle
import os
import time                                                       #1


class Programmer(object):
    """
    Programmer that solves problems

    Problems are contained in tasks.
    Tasks are received from the problem owner.
    """

    def __init__(self,                                            #2
                 name,
                 age,
                 skill_level,
                 world_time,
                 pickle_path=None):
        """
        Make a new programmer.

        hint: worldtime is instance of
        programmersworld.worldtime.WorldTime
        """
        self.name = name
        self.age = age
        self.__skill_level = skill_level
        self.world_time = world_time
        self.tasks = []
        self.current_task = None
        self.start = time.time()
        self.finished_tasks = []
        if not pickle_path:
            own_dir = os.path.dirname(__file__)
            self.pickle_path = os.path.join(own_dir, 'data', 'daily.pcl')
        else:
            self.pickle_path = pickle_path

    def set_skill_level(self, level):                             #3
        """Make sure the skill level can be converted to an integer.
        """
        self.__skill_level = int(level)

    def get_skill_level(self):
        """Return current skill level.
        """
        return self.__skill_level                                 #4

    def __set_current_task(self):                                 #5
        """Set first task in task list as current task.
        """
        try:
            self.current_task = self.tasks[0]
        except IndexError:
            self.current_task = None
        if len(self.tasks) > 0:
            self.tasks = self.tasks[1:]

    def add_task(self,
                problem_name,
                problem_work_load):
        """"Add task to list of tasks."""
        self.tasks.append(Task(problem_name,                      #6
                               problem_work_load))

    def work(self):
        """Work, i.e. solving the problem is done here.

            If the current task is not finished
            and it is working time, the problem is solved
            by asking the task object to do so.
        """
        if not self.current_task:
            self.__set_current_task()
        finished = False                                          #7
        show_break = True
        has_pickle = False
        while not finished:                                       #8
            task_finished = False
            if self.world_time.get_is_work_time():                #9
                if has_pickle:
                    self.read_pickle()
                    has_pickle = False
                task_finished = self.current_task.solve()
                show_break = True
            else:                                                 #10
                if show_break:
                    self.write_pickle()
                    has_pickle = True
                    print()
                    print(self.world_time.date)
                    print('Pausing!')
                    show_break = False
            self.world_time.do_step()                             #11
            if task_finished:                                     #12
                self.finished_tasks.append(self.current_task)
                self.report()
                self.__set_current_task()
            if not self.tasks:
                break                                             #13
        print()
        print('Finished all tasks!')

    def write_pickle(self):
        """Write current state to pickle file."""
        pickle_dict = {}
        pickle_dict['current_task'] = self.current_task
        pickle_dict['tasks'] = self.tasks
        pickle_dict['finished_tasks'] = self.finished_tasks
        fobj = open(self.pickle_path, 'wb')
        pickle.dump(pickle_dict, fobj)
        fobj.close()
        print('Data pickled')

    def read_pickle(self):
        """Read state from pickle file."""
        fobj = open(self.pickle_path, 'rb')
        pickle_dict = pickle.load(fobj)
        self.current_task = pickle_dict['current_task']
        self.tasks = pickle_dict['tasks']
        self.finished_tasks = pickle_dict['finished_tasks']
        fobj.close()
        print('Data read from pickle')

    def report(self):                                             #14
        """Produce screen print of activity."""
        print()
        print(self.world_time.date)
        print('Finished %d tasks.' % (len(self.finished_tasks)))
        print('%d tasks remaining' % (len(self.tasks)))


class Task(object):                                               #15
    """
    Tasks are received from the problem owner.

    A task has a name and a workload.
    The workload is the time in hours
    required to complete the task.
    Examples for typical workloads are:
    very low            10
    low                 30
    medium              50
    high                70
    very high           90
    extremly high      100
    Workloads over 100 are rejected
    because programmers are smart people.
    """

    def __init__(self,
                 name,
                 work_load):
        """Make a new task.

        Only tasks with a work load <= 100 are allowed.
        """
        if work_load > 100:                                       #16
            print('Workload: %d' % work_load)
            raise OverflowError('Workloads over 100 are not allowed')
        self.name = name
        self.work_load = work_load
        self.work_step = 0.5
        self.finished = False

    def solve(self):
        """Solve a task

        We just substract the work step.
        The skill level of the programmer is NOT
        considered.
        """
        self.work_load -= self.work_step                          #17
        if self.work_load <= 0:
            self.finished = True                                  #18
        return self.finished
