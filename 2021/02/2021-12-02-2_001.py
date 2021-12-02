"""
Lines of code: medium
Readability: high
Efficiency: medium

Initial naive version.
10 lines of code, readable, walks the data set twice though.
"""

cmds = [(line.split()) for line in open("input")]

aim, horiz, depth = 0, 0, 0
for cmd in cmds:
    if cmd[0] == "up":
        aim -= int(cmd[1])
    elif cmd[0] == "down":
        aim += int(cmd[1])
    else:
        horiz += int(cmd[1])
        depth += aim * int(cmd[1])

print(f"{horiz*depth}")