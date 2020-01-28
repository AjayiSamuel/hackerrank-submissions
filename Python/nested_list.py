# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]


def second_lowest_grade_finder(students):
    scores = []
    second_min_score = None
    for i in range(len(students)):
        scores.append(students[i][1])

    scores.sort(reverse=False)

    for i in range(len(scores)-1):
        if scores[i] != scores[i+1]:
            second_min_score = scores[i+1]
            break

    second_lowwest_students = [student[0] for student in students if student[1] == second_min_score]
    if len(second_lowwest_students) > 1:
        second_lowwest_students.sort()
    print(*second_lowwest_students, sep="\n")


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second_lowest_grade_finder(students)


# test = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7]
# scores = [37.2, 37.21, 37.21, 39, 41]
# def second_min_score(scores):
#     for i in range(len(scores)-1):
#         if scores[i] != scores[i+1]:
#             second_min_score = scores[i+1]
#             break
#         else:
#             pass
#     return second_min_score
#
#
# print(second_min_score(scores))
# print(second_min_score(test))






# max = scores.pop(max(scores))
# print("max score: ", max)
# second_max = scores.pop(max(scores))
# print("second max score: ", max)