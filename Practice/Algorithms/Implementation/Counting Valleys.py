#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
# We only care about the number of valleys... So just figure out the number of times you came back up to sea level.
def countingValleys(n, s):
    valley = 0
    lvl = 0  # current level
    for i in s:
        if (i == 'U'):
            lvl += 1
        if (i == 'D'):
            lvl -= 1

        # if we just came UP to sea level
        if (lvl == 0 and i == 'U'):
            valley += 1

    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()