#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module for Programmer's World time (PWT).

PWT is expressed as a fraction of real time.
"""

from __future__ import print_function, unicode_literals

import datetime
import time
import os

from .timeio import read_times

PWT_TO_REALTIME_RATIO = 1e5 # times faster                        #1
TIME_STEP_IN_HOURS = 0.1
TIMES_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                          '../data/times.txt')


class WorldTime(object):
    """Representation of programmers world time.
    """

    week_day_map = {0: 'Monday',                                  #2
                    1: 'Tuesday',
                    2: 'Wednesday',
                    3: 'Thursday',
                    4: 'Friday',
                    5: 'Saturday',
                    6: 'Sunday'}

    def __init__(self, date):                                     #3
        """Intialize start date.
        """
        self.date = date                                          #4
        # real hours                                              #5
        self.time_step = datetime.timedelta(hours=TIME_STEP_IN_HOURS)
        self.simulation_time_step = (                             #6
            TIME_STEP_IN_HOURS * 3600.0 /
            PWT_TO_REALTIME_RATIO) # in seconds
        self.work_hours = read_times(file_name=TIMES_PATH)        #7

    def do_step(self):                                            #8
        """Do one simulation time step.
        """
        self.date += self.time_step
        time.sleep(self.simulation_time_step)

    def get_is_work_time(self):                                   #9
        """Find out if programmer is supposed to work.
        """
        week_day = self.week_day_map[self.date.weekday()]
        try:                                                      #10
            time_slot = self.work_hours[week_day]
        except KeyError:
            return False
        current_time = self.date.hour + self.date.minute / 60.0
        if time_slot[0] <= current_time <= time_slot[1]:          #11
            return True
        else:
            return False

# self test code
if __name__ == '__main__':                                        #12

    def test():
        """Check if works as expected.
        """
        world_time = WorldTime(datetime.datetime.today())
        print(world_time.date.weekday())
        for step in range(1000):
            print(world_time.date.isoformat())
            world_time.do_step()
            if world_time.get_is_work_time():
                print('It is working time!')

    test()
