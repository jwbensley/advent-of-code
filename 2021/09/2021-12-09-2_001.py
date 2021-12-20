"""
Lines of code: 
Readability: 
Efficiency: 


"""

import math
width = len(list(open("input"))[0].strip())
values = [int(num) for line in open("input") for num in line.strip()]
rows = (len(values) // width) -1


def search(x, y, basin):
    if (x,y) in basin:
        return basin

    if (x > 0
        and values[x + (y*width)] != values[(x - 1) + (y*width)]
        and values[(x - 1) + (y*width)] != 9):
            basin.add((x,y))
            basin.update(search(x-1, y, basin))

    if (x < (width -1)
        and values[x + (y*width)] != values[(x + 1) + (y*width)]
        and values[(x + 1) + (y*width)] != 9):
            basin.add((x,y))
            basin.update(search(x+1, y, basin))

    if (y > 0
        and values[x + (y*width)] != values[x + ((y-1)*width)]
        and values[x + ((y-1)*width)] != 9):
            basin.add((x,y))
            basin.update(search(x, y-1, basin))

    if (y < rows
        and values[x + (y*width)] != values[x + ((y+1)*width)]
        and values[x + ((y+1)*width)] != 9):
            basin.add((x,y))
            basin.update(search(x, y+1, basin))

    return basin

basins = []
for idx, value in enumerate(values):

    if value == 9:
        continue

    basin = search((idx % width), (idx // width), set())
    if basin not in basins:
        basins.append(basin)

print(math.prod(sorted([len(basin) for basin in basins])[-3:]))