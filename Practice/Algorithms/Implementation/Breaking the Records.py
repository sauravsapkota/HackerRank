#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_count = 0
    min_count = 0
    max = min = scores[0]

    for i in scores:
        if i > max:
            max = i
            max_count += 1

        if i < min:
            min = i
            min_count += 1

    min_max = [max_count,min_count]
    return min_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()