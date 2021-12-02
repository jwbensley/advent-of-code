"""
Lines of code: medium
Readability: medium
Efficiency: high

10 lines of code, quite readable, walks the data set only once.
"""

aim, horiz, depth = 0, 0, 0
for line in open("input"):

    if line.split()[0] == "up":
        aim -= int(line.split()[1])
    elif line.split()[0] == "down":
        aim += int(line.split()[1])
    else:
        horiz += int(line.split()[1])
        depth += aim * int(line.split()[1])

print(f"{horiz*depth}")