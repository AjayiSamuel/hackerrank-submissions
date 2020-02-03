import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    valley_count = 0
    valley = False
    for step in s:
        if step == 'D':
            height -= 1
            if height < 0 and valley is False:
                valley = True
                valley_count += 1

        if step == 'U':
            height += 1
            if height >= 0 and valley == True:
                valley = False

    return valley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()

# Sample input
# 8
# UDDDUDUU

# # c = list(map(lambda b: b.replace("1", "10"), a))