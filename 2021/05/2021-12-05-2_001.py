"""
Lines of code: Medium
Readability: High
Efficiency: Medium

Lines of code isn't super high, and easy to read, but it's a brute force method
using a load of "if" statements. But it's moderately efficient, the data set is
only walked once on input, then the grid is scanned at the end.
"""

width = 999
grid = [0 for i in range(0, (width*width))]
danger_points = 0

for line in open("input"):
    x1, y1 = map(int, line.split()[0].split(","))
    x2, y2 = map(int, line.split()[2].split(","))

    if (x1 > x2) and (y1 == y2):
        for x in range(x2, x1+1):
            grid[x + (y1 * width)] += 1

    elif (x1 < x2) and (y1 == y2):
        for x in range(x1, x2+1):
            grid[x + (y1 * width)] += 1

    elif (y1 > y2) and (x1 == x2):
        for y in range(y2, y1+1):
            grid[x1 + (y * width)] += 1

    elif (y1 < y2) and (x1 == x2):
        for y in range(y1, y2+1):
            grid[x1 + (y * width)] += 1

    elif (x1 < x2) and (y1 < y2): # Down right
        y = y1
        for x in range(x1, x2+1):
            grid[x + (y * width)] += 1
            y += 1

    elif (x1 > x2) and (y1 < y2): # Down left
        y = y2
        for x in range(x2, x1+1):
            grid[x + (y * width)] += 1
            y -= 1

    elif (x1 > x2) and (y1 > y2): # Up left
        y = y2
        for x in range(x2, x1+1):
            grid[x + (y * width)] += 1
            y += 1

    elif (x1 < x2) and (y1 > y2): # Up right
        y = y1
        for x in range(x1, x2+1):
            grid[x + (y * width)] += 1
            y -= 1

for i in range(0, width):
    print(grid[i*width:(i+1)*width])

print(sum([1 for i in grid if i > 1]))