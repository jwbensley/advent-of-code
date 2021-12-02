"""
Lines of code: low
Readability: high
Efficiency: medium

It's only five lines of code, perfectly readable, and we only walk the
measurements list twice.
"""

measurements = [int(line.strip()) for line in open("input")]

count = 0
for i in range(1, len(measurements)):
    count += int(measurements[i] > measurements[i-1])
print(count)