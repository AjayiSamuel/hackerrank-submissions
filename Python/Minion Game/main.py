# def minion_game(string):
#     # your code goes here
#     string
#
#
# if __name__ == '__main__':
#     s = raw_input()
#     minion_game(s)


class FE:
    def __init__(self, tag, year):
        self.tag = tag
        self.year = year

    def __str__(self):
        return f"{self.tag}, {self.year}"


tag = [1,2]
year = 1
bt = FE(tag,year)
print(bt)
tag.append(3)
year = 2
print(bt)


# class FunEvent:
#     def __init__(self, tags, year):
#         self.tags = tags
#         self.year = year
#
#     def __str__(self):
#         return f"FunEvent(tags={self.tags}, year={self.year})"
#
#
# tags = ["google", "ml"]
# year = 2022
# bootcamp = FunEvent(tags, year)
# tags.append("bootcamp")
# year = 2023
# print(bootcamp)

# def sqsum1():
# 	return sum(x**2 if x > 0 for x in nums)
#
# def sqsum2():
#   	return sum(x^2 for x in nums if x > 0)
#
# def sqsum3():
#   	return sum(for x in nums if x > 0 then x^2)
#
# def sqsum4():
#   	return sum(x**2 for x in nums if x > 0)
#
# def sqsum5():
#   	return sum(x^2 if x > 0 for x in nums)