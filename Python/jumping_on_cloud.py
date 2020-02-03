# Complete the jumpingOnClouds function below.


def jumpingOnClouds():
    ans = 0
    i = 0
    while i < n - 1:
        if i + 2 >= n or c[i + 2] == 1:
            i = i + 1
            ans = ans + 1
        else:
            i = i + 2
            ans = ans + 1
    return ans

if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds()
    print(result)

# 6
# 0 0 0 0 1 0
# sample output: 3