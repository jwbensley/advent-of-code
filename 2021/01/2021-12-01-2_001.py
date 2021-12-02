"""
Lines of code: medium
Readability: medium
Efficiency: medium

It's only five lines of code, it's readable, and the effort is only 2n,
which is "OK".
"""

m = [int(line.strip()) for line in open("input")]

count = 0
for i in range(2, len(m)-1):
    count += int((m[i] + m[i-1] + m[i-2]) < (m[i+1] + m[i] + m[i-1]))
print(count)