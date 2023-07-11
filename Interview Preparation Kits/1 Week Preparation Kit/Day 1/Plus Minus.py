#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count = len(arr)

    p_count = sum(1 for num in arr if num > 0)  # Use generator expression and sum function
    n_count = sum(1 for num in arr if num < 0)
    z_count = count - p_count - n_count  # Calculate zero count directly

    # Print formatted output using f-strings
    print(f'{p_count / count:.6f}')
    print(f'{n_count / count:.6f}')
    print(f'{z_count / count:.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
