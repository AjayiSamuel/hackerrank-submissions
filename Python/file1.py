def getMinimumUniqueSum(arr):
    # Write your code here
    sm = arr[0]
    for i in range(1, arr_count):
        if arr[i] == arr[i - 1]:
            j = i
            while j < arr_count and arr[j] <= arr[j - 1]:
                arr[j] = arr[j] + 1
                j += 1
        sm = sm + arr[i]
    return sm


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getMinimumUniqueSum(arr)
    print(result)