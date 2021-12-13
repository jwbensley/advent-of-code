"""
Lines of code: low
Readability: medium
Efficiency: high

Only 9 lines of code.
Readability is OK.
The data set is only walked once after reading, but int() is called n*12 times.
"""

no_of_ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lines = [line.strip() for line in open("input")]
for line in lines:
    for i in range(0, 12):
        no_of_ones[i] += int(line[11-i])

gamma = 0
for i in range(len(no_of_ones) - 1, -1, -1):
    gamma |= int(not bool((len(lines) / 2) // no_of_ones[i])) << i

print(gamma * (~gamma & 0xFFF))