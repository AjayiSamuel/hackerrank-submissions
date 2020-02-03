#!/bin/python3
import re


# Complete the repeatedString function below.
def repeatedString(s, n):
    len_str = len(s)
    no_a = len(re.findall('a', s))
    multiplier,  reminder = int(n/len(s)), n % len_str
    all_a = no_a * multiplier
    all_a += len(re.findall('a', s[:reminder]))
    return all_a


if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(result)

# sample input
# aba
# 10

# sample input 2
# a
# 1000000000000

# alternate function for smaller sized strings
# def repeatedString(s, n):
#     # for x in range(n):
#     #     s+=s
#     #     if len(s) > n:
#     #         break
#     #
#     # s = s[0:n]
#     # x = re.findall("a", s)
#     # return len(x)

