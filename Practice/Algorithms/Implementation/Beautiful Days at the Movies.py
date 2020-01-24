#!/bin/python3

import os


# Python Program to Reverse a Number using While loop
def reverse(num):
    rev = 0
    while (num > 0):
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10

    return rev


# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0

    for num in range(i, j + 1):
        rev = reverse(num)
        if (abs(num - rev) % k) == 0:
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
