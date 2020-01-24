#!/bin/python3

import os


# Complete the hurdleRace function below.
def hurdleRace(k, height):
    max_height = max(height)
    if k < max_height:
        potion = max_height - k
    else:
        potion = 0

    return potion


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
