import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    the_sum = []
    for row in range(len(arr)-2):
        # print(arr[i])
        for column in range(len(arr)-2):
            the_sum.append(sum([
                arr[row][column], arr[row][column+1], arr[row][column+2],
                arr[row+1][column+1],
                arr[row+2][column], arr[row+2][column + 1], arr[row+2][column + 2]]
            ))

    return max(the_sum)


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print(result)
