def hashing(n, int_list):
    int_tuple = tuple(int_list)
    return hash(int_tuple)


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hashing(n, integer_list))


# sample data
# 2
# 1 2
# output:
# 3713081631934410656