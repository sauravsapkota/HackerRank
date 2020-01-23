#!/bin/python3

import os


# Complete the 'pickingNumbers' function below.
def pickingNumbers(a):
    a.sort()
    max = 0

    for i in range(len(a) - 1, 1, -1):
        count = 1
        j = i - 1
        while j >= 0:
            if ((a[i] - a[j]) < 2):
                count += 1

            j -= 1

            max = count if count > max else max

    return max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
