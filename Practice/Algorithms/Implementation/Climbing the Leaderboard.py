# !/bin/python3

import os


# solved by applying binary search
# It won't exactly be like normal binary search for sure. Here's my modification which passed all the test cases.
def binarySearch(alice, scores):
    low = 0
    high = len(scores) - 1

    while (low <= high):
        mid = (high + low) // 2
        if (scores[mid] == alice):
            return mid
        elif (scores[mid] < alice and alice < scores[mid - 1]):
            return mid
        elif (scores[mid] > alice and alice >= scores[mid + 1]):
            return mid + 1
        elif (scores[mid] < alice):
            high = mid - 1
        elif (scores[mid] > alice):
            low = mid + 1

    return -1


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    i = 0
    print(len(scores) - 1)
    ranks = []
    results = []
    rank = 1
    score = scores[0]
    for s in scores:
        if s != score:
            rank += 1

        score = s
        ranks.append(rank)

    for a in alice:
        print("Alice = " + str(a))
        if a > scores[0]:
            results.insert(i, 1)
        elif a < scores[len(scores) - 1]:
            results.insert(i, ranks[len(scores) - 1] + 1)
        else:
            index = binarySearch(a, scores)
            results.insert(i, ranks[index])

        i += 1

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))
    print(scores, alice)
    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
