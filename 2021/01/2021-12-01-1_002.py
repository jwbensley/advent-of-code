"""
Lines of code: low
Readability: medium
Efficiency: medium

It's only two lines of code, not super unreadable but not great, and we only
walk the measurements list twice.
"""

measurements = [int(line.strip()) for line in open("input")]
print(sum([1 for i in range(1, len(measurements)) if int(measurements[i] > measurements[i-1])]))