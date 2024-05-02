def swap_case(s):
    switched_string = str()
    for char in s:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
            elif char.islower():
                char = char.upper()
        switched_string += char
    return switched_string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)