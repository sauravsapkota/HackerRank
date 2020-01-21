#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def myround(i):
    return i + (5 - i) % 5

def gradingStudents(grades):
    list = []

    for i in grades:
        if i >= 38:
            if(myround(i) - i >= 3):
                list.append(i)
                # print(i)
            else:
                list.append(myround(i))
                # print(myround(i))
        else:
            list.append(i)
            # print(i)
    # print(list)
    return list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()