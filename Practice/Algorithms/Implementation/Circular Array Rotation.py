#!/bin/python3

import os


def circularArrayRotation(a, k, queries):
    results = []

    # Rotate the given array by n times toward right
    for i in range(0, k):
        # Stores the last element of array
        last = a[len(a) - 1]

        for j in range(len(a) - 1, -1, -1):
            # Shift element of array by one
            a[j] = a[j - 1]

        # Last element of the array will be added to the start of the array.
        a[0] = last

    for i in queries:
        # print(i)
        results.append(a[i])

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
