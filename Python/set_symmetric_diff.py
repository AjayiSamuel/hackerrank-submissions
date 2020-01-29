def no_of_exclusive_stds(set_1, set_2):
    english_students, french_student = set_1, set_2
    print(len(english_students.symmetric_difference(french_student)))


if __name__ == "__main__":
    number_of_eng_student = input()
    eng = set(map(int, input().split()))
    # print(eng_students)
    number_of_french_student = input()
    french = set(map(int, input().split()))
    no_of_exclusive_stds(eng, french)