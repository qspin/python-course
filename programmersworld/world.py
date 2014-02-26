#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Main program of programmers world.

A programmer needs to solve the problems, which
a problemowner creates. The problems become tasks, i.e.
become solveable and are solved in a certain amount of time.
Time functionality is provided by
programmersworld.tools.worldtime.
"""

import datetime                                                   #1
from optparse import OptionParser
import os
import sys


# pylint: disable-msg=C0103
# Get grand parent directory and put on Pythons search
# path for modules.
# This makes the package runable without installation.
dirn = os.path.dirname
sys.path.append(dirn(dirn(os.path.abspath(__file__))))

import programmersworld.problemowners as powners                  #2
from programmersworld import programmers
from programmersworld.tools.worldtime import WorldTime


def main():                                                       #3
    """Main function that starts the simulation.

    Hint: The name does NOT need to be main.
    Any other name is fine.
    """
    parser = OptionParser()
    parser.add_option("-n", "--name",
                      dest="name_of_problem_owner",
                      type="string",
                      help="name of problem owner")
    (options, args) = parser.parse_args()
    today = datetime.datetime.today()                             #4
    world_time = WorldTime(today)                                 #5
    problem_owner = powners.ProblemOwner(                         #6
                   options.name_of_problem_owner)
    programmer = programmers.Programmer(name='Bill',              #7
                                        age=35,
                                        skill_level=50.0,
                                        world_time=world_time)

    for counter in range(10):                                     #8
        problem_name, problem_work_load = problem_owner.make_problem()
        programmer.add_task(problem_name, problem_work_load)

    programmer.work()                                             #9

if __name__ == '__main__':                                        #10
    main()
