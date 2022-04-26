# Terminated due to timeout
# !/bin/python3

import os


def min(list):
    min_val = 10000000
    for i in list:
        if min_val > i and i > 0:
            min_val = i

    return min_val


# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    while True:
        sticks = 0
        minimum = min(arr)
        for i in range(0, len(arr)):
            if arr[i] >= min(arr):
                sticks += 1

            arr[i] -= minimum

        if (all(elem <= 0 for elem in arr)):
            break


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
