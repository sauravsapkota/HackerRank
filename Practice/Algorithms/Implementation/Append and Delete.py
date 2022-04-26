#!/bin/python3

import os


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    common_length = 0

    for i, j in zip(s, t):
        if i == j:
            common_length += 1
        else:
            break

    # CASE A
    if ((len(s) + len(t) - 2 * common_length) > k):
        return "No"
    # CASE B
    elif ((len(s) + len(t) - 2 * common_length) % 2 == k % 2):
        return "Yes"
    # CASE C
    elif ((len(s) + len(t) - k) < 0):
        return "Yes"
    # CASE D
    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
