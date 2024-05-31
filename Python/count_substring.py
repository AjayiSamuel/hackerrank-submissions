def count_substring(string, sub_string):
    counter = 0
    size = len(sub_string)
    for i in range(len(string)):
        if sub_string == string[i:size+i]:
            counter += 1
    return counter


print(count_substring("ABCDCDC", "CDC"))
