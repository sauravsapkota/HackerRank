#!/bin/python3

import os


# Complete the findDigits function below.
def findDigits(n):
    count = 0
    digits = []

    for d in str(n):
        digits.append(int(d))

    for d in digits:
        if d != 0:
            if n % d == 0:
                count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
