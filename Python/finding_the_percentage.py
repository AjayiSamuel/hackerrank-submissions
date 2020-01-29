# student_mark = {'sam': [72.0, 68.0, 69.0]}
#
# query_name = 'sam'


def find_average_percentage(student_marks, query_name):
    student_marks = student_marks
    scores = student_marks[query_name]
    avg = sum(scores) / len(scores)
    return avg


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print("%.2f" % find_average_percentage(student_marks, query_name))


# print("%.2f" % round(a,2))