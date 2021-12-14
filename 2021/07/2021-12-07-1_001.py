"""
Lines of code: Low
Readability: Medium
Efficiency: High

4 lines of code of pretty low. Readability is just about OK, any more
compression and it would be low. The input data set is only walked once so
efficiency is high.
"""

import statistics
values = list(map(int, [line.strip().split(",") for line in open("input")][0]))
median = int(statistics.median(values))
print(sum([abs(value - median) for value in values]))