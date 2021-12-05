"""
Lines of code: low
Readability: medium
Efficiency: medium

Initial naive version.
Only 15 lines of code.
Readability is just about OK, any more compression would probably qualify
as "low".
The input file is read once, but the data set is then walked twice.
"""

nums = [line.strip() for line in open("input")]

def find_number(numbers, most):
    i = 0
    while(len(numbers) > 1):

        no_of_ones = sum([int(num[i]) for num in numbers])

        if no_of_ones >= (len(numbers) / 2):
            most_common = 1
        else:
            most_common = 0

        for num in numbers[:]:
            if num[i] != str((lambda x: most_common if x else int(not most_common))(most)):
                numbers.remove(num)
        i += 1

    return int(numbers[0], 2)

print(find_number(nums[:], 1) * find_number(nums[:], 0))