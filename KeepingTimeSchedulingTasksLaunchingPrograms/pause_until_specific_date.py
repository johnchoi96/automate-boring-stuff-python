#!/usr/bin/python3

import datetime
import time

halloween2020 = datetime.datetime(2020, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2020:
    time.sleep(1)

"""
THe time.sleep(1) call will pause the Python program so that the computer does not waste CPU resources
by checking the time over and over. Instead, the while loop will just check the condition once per second and continue
with the rest of the program after halloween 2020
"""