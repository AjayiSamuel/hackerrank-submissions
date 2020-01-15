def print_n(n):
    nums = []
    for i in range(n):
        nums.append(i+1)

    print(*nums, sep="")


if __name__ == '__main__':
    n = int(input())
    print_n(n)
