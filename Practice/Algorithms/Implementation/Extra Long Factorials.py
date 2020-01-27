#!/bin/python3


# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    factorial = 1
    # check if the number is negative, positive or zero
    if n < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif n == 0:
        print(1)
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        print(factorial)


if __name__ == '__main__':
    fact = 0
    n = int(input())

    extraLongFactorials(n)
