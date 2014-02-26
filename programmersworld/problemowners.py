#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Home of the class ProblemOnwer
"""

from __future__ import print_function, unicode_literals

import random                                                     #1


class ProblemOwner(object):                                       #2
    """
    A ProblemOwner creates problems.
    """
    problem_limit = 100

    def __init__(self, name):                                     #3
        """
        Set intial values.
        """
        self.name = name                                          #4
        self.satisfied = False                                    #5
        self.problem_counter = 0                                  #6

    def make_problem(self, name=None):                            #7
        """
        Create a problem.

        If no problem name is given,
        use problem_counter as name.
        """
        self.satisfied = False                                    #8
        self.problem_counter += 1                                 #9
        if not name:
            name = str(self.problem_counter)                      #10
        return name, int(random.random() * 100)                   #11

    def receive_solution(self):
        """Make the problem owner satisfied.
        """
        self.satisfied = True                                     #12

    def __str__(self):                                            #13
        return '\nMy name is %s.\n' \
               'I am a problemowner.' % self.name


if __name__ == '__main__':                                        #14
    # Only executed if started on commandline.

    def report(name, satisfied):                                  #15
        """Helper function for test
        """
        if satisfied:
            print('%s is satisfied.' % name)
        else:
            print('%s is not satisfied.' % name)

    def test():
        """Test if it works.
        """
        problem_owner = ProblemOwner('Paul')                      #16
        report(problem_owner.name, problem_owner.satisfied)
        problem_name, work_load = problem_owner.make_problem()
        print(problem_name, work_load)                            #17
        report(problem_owner.name, problem_owner.satisfied)
        problem_owner.receive_solution()                          #18
        report(problem_owner.name, problem_owner.satisfied)
        print(problem_owner)
        print(problem_owner.__dict__)                              #19


    test()
