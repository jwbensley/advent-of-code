"""
Lines of code: medium
Readability: high
Efficieny: medium

It's only six lines of code, perfectly readable, and we only walk the
measurements list twice.
"""

with open("input") as f:
    measurements = [int(line) for line in f]

count = 0
for i in range(1, len(measurements)):
    count += int(measurements[i] > measurements[i-1])

print(count)