"""
Lines of code: low
Readability: high
Efficiency: medium

It's only six lines of code, perfectly readable, and we only walk the
measurements list once.
"""

last = 999999999
count = 0
for line in open("input"):
        count += int(int(line.strip()) > last)
        last = int(line.strip())
print(count)