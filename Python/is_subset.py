def check_subset(num, a_sets, b_sets):
    check_value = []
    for x in range(num):
        check_value.append(a_sets[x].issubset(b_sets[x]))

    return check_value


if __name__ == "__main__":
    num = int(input())
    a_sets = []
    b_sets = []
    for _ in range(num):
        no_of_set_a = int(input())
        set_1 = set(map(int, input().split()))
        a_sets.append(set_1)
        no_of_set_b = int(input())
        set_2 = set(map(int, input().split()))
        b_sets.append(set_2)

    print(*check_subset(num, a_sets, b_sets), sep="\n")


# sample data

# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
