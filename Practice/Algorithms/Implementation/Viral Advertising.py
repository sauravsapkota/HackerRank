#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared = 5
    liked = shared//2
    cumulative = liked

    for i in range(2,n+1):
        shared = liked * 3
        liked = shared//2
        cumulative += liked

    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()