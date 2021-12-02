"""
Lines of code: low
Readability: medium
Efficiency: high

4 lines of code, quite readable, walks the data set only once, but it does
call split() 2n times.
"""

totals = {"forward": 0, "up": 0, "down": 0}
for line in open("input"):
    totals[line.split()[0]] += int(line.split()[1])
print(f"{totals['forward']*(totals['down']-totals['up'])}")