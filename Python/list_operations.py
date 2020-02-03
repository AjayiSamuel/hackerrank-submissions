def list_operation(n, operations):
    custom_list = []
    for i in range(len(operations)):
        if operations[i][0] == 'insert':
            custom_list.insert(int(operations[i][1]), int(operations[i][2]))
        if operations[i][0] == 'print':
            print(custom_list)
        if operations[i][0] == 'remove':
            custom_list.remove(int(operations[i][1]))
        if operations[i][0] == 'append':
            custom_list.append(int(operations[i][1]))
        if operations[i][0] == 'sort':
            custom_list.sort()
        if operations[i][0] == 'pop':
            custom_list.pop()
        if operations[i][0] == 'reverse':
            custom_list.reverse()


if __name__ == '__main__':
    operations = []
    N = int(input())
    for _ in range(N):
        action = input().split(" ")
        operations.append(action)

    list_operation(N, operations)

# sample data

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# output:

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]