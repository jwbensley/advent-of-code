"""
Lines of code: Low
Readability: High
Efficiency: Medium

11 lines of code. Easy to read.
The input file is walked once, then the same data is walked to get the totals,
then again to calculate the 256 days, probably could be better.
"""

fish_days = list(map(int, [line.strip().split(",") for line in open("input")][0]))
totals = [0] * 9

for fish in fish_days:
    totals[fish] += 1

for i in range(256):
    zero_total = totals[0]
    for j in range(8):
        totals[j] = totals[j+1]
    totals[6] += zero_total
    totals[8] = zero_total

print(sum(totals))