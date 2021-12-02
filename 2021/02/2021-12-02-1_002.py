"""
Lines of code: medium
Readability: medium
Efficiency: medium

10 lines of code, a bit less readable, walks the data set twice though and
calls split() twice as often.
"""

cmds = [(line.split()[0], int(line.split()[1])) for line in open("input")]

horiz, depth = 0, 0
for cmd in cmds:
    if cmd[0] == "up":
        depth -= cmd[1]
    elif cmd[0] == "down":
        depth += cmd[1]
    else:
        horiz += cmd[1]

print(f"{horiz*depth}")