"""
Lines of code: low
Readability: medium
Efficiency: medium

Only 21 lines of code.
Readability is OK.
The data set is only walked once, but int() is called n*12 times.
"""

no_of_ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lines = 0
for line in open("input"):

    line = line.strip()
    lines += 1
    no_of_ones[0] += int(line[11])
    no_of_ones[1] += int(line[10])
    no_of_ones[2] += int(line[9])
    no_of_ones[3] += int(line[8])
    no_of_ones[4] += int(line[7])
    no_of_ones[5] += int(line[6])
    no_of_ones[6] += int(line[5])
    no_of_ones[7] += int(line[4])
    no_of_ones[8] += int(line[3])
    no_of_ones[9] += int(line[2])
    no_of_ones[10] += int(line[1])
    no_of_ones[11] += int(line[0])

gamma, epsilon = 0, 0
for i in range(len(no_of_ones) - 1, -1, -1):
    gamma |= int(not bool((lines / 2) // no_of_ones[i])) << i
    #epsilon |= int(bool((lines / 2) // no_of_ones[i])) << i

print(gamma * (~gamma & 0xFFF))