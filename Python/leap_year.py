# function to check is a given year is a leap year of not
# constraint- 1900 to 10^5

def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
        else:
            leap = True

    return leap


year = int(input())
print(is_leap(year))