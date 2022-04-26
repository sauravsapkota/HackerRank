#!/bin/python3

# import math
import os
import random
import re
import sys
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if(s[-2]+s[-1] == "PM"):
        time = int(s[0] + s[1])
        if time != 12:
            time = int(s[0] + s[1]) + 12
    elif (s[-2] + s[-1] == "AM"):
        time = int(s[0] + s[1])
        if time == 12:
            time = int(s[0] + s[1]) - 12
    strtime = "{:02d}".format(time)
    return strtime+s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
