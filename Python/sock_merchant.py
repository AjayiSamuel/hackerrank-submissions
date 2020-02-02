import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
# sample data:
# 9
# 10 20 20 10 10 30 50 10 20


def sockMerchant(n, ar):
    # sock_type = set(ar)
    # sock_dict = {sock:num for sock in set(ar) for x in }
    sock_dict = Counter(ar)
    count = []
    for num in sock_dict.values():
        count.append(int(num/2))
    return sum(count)

def sockMerchant_without_Counter(n, ar):
    sock_dict = {}

    for i in ar:
        if i in sock_dict:
            sock_dict[i] += 1
        else:
            sock_dict[i] = 1

    val = 0
    for num in sock_dict.values():
        val += (num // 2)

    return val


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(input())
#     ar = list(map(int, input().rstrip().split()))
#     result = sockMerchant(n, ar)
#     fptr.write(str(result) + '\n')
#     fptr.close()

# to test feature without Counter run line below
print(sockMerchant_without_Counter(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
