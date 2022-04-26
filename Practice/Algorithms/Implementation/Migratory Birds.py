#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    type_1 = 0
    type_2 = 0
    type_3 = 0
    type_4 = 0
    type_5 = 0
    for i in arr:
        if i == 1:
            type_1 += 1

        elif i == 2:
            type_2 += 1

        elif i == 3:
            type_3 += 1

        elif i == 4:
            type_4 += 1

        elif i == 5:
            type_5 += 1

        else:
            print('Error')

    count = [type_1, type_2, type_3, type_4, type_5]

    m = max(count)

    for i in range(0, len(count)):
        if count[i] == m:
            answer = i + 1
            break

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()