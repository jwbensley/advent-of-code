"""
Lines of code: medium
Readability: medium
Efficiency: high

9 lines of code, quite readable, walks the data set only once.
"""

horiz, depth = 0, 0
for line in open("input"):

    if line.split()[0] == "up":
        depth -= int(line.split()[1])
    elif line.split()[0] == "down":
        depth += int(line.split()[1])
    else:
        horiz += int(line.split()[1])

print(f"{horiz*depth}")