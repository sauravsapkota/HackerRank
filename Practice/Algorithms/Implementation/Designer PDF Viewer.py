#!/bin/python3

import os


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    max_h = 0

    for w in word:
        if h[ord(w) - 97] > max_h:
            max_h = h[ord(w) - 97]

    return max_h * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
