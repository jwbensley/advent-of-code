"""
Lines of code: Low
Readability: Medium
Efficiency: High

5 lines of code of pretty low. Readability is just about OK, any more
compression and it would be low. The input data set is only walked once so
efficiency is high.
"""

import math
import statistics
values = list(map(int, [line.strip().split(",") for line in open("input")][0]))
mean = math.floor(statistics.mean(values))
print(sum([(abs(value - mean)*(abs(value - mean)+1)//2) for value in values]))