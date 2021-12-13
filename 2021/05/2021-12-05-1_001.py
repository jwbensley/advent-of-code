"""
Lines of code: 
Readability: 
Efficiency: 


"""

width = 999
grid = [0 for i in range(0, (width*width))]
danger_points = 0
for line in open("input"):
    x1, y1 = map(int, line.split()[0].split(","))
    x2, y2 = map(int, line.split()[2].split(","))

    if (x1 != x2) and (y1 != y2):
        continue

    if x1 > x2:
        for i in range(x2, x1+1):
            grid[i + (y1 * width)] += 1

    elif x1 < x2:
        for i in range(x1, x2+1):
            grid[i + (y1 * width)] += 1

    elif y1 > y2:
        for i in range(y2, y1+1):
            grid[x1 + (i * width)] += 1

    elif y1 < y2:
        for i in range(y1, y2+1):
            grid[x1 + (i * width)] += 1

print(sum([1 for i in grid if i > 1]))