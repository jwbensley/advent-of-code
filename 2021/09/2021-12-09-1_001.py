"""
Lines of code: High
Readability: High
Efficiency: Medium


Initial ugly solution to understand the problem.
I'm sure it can be done in a lot fewer lines of code, also the input file is
read twice, and then the data set loops over, so three iterations of the data
in total.
"""

width = len(list(open("input"))[0].strip())
heights = [int(num) for line in open("input") for num in line.strip()]
rows = (len(heights) // width) -1
row = 0
lowest = []

for idx, height in enumerate(heights):
    UP, DOWN, LEFT, RIGHT = False, False, False, False
    if row > 0:
        if height < heights[idx - width]:
            UP = True
    else:
        UP = True

    if row < rows:
        if height < heights[idx + width]:
            DOWN = True
    else:
        DOWN = True

    if idx < (((row + 1) * width) - 1):
        if height < heights[idx + 1]:
            RIGHT = True
    else:
        RIGHT = True

    if idx > (row * width):
        if height < heights[idx - 1]:
            LEFT = True
    else:
        LEFT = True

    if UP and DOWN and LEFT and RIGHT:
        lowest.append(height)

    if idx == (((row + 1) * width) -1):
        row += 1

print(sum(lowest) + len(lowest))