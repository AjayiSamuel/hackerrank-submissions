def runner_up_score(arr):
    numbers = list(arr)
    max_num = max(numbers)
    numbers = [x for x in numbers if x != max_num]
    new_max = max(numbers)
    return new_max


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(runner_up_score(arr))