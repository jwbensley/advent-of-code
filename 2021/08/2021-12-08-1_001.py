"""
Lines of code: Low
Readability: Medium
Efficiency: High

Doesn't get much shorter than 1 line of code, but it has come at the cost of
some readability, but the readability is still OK. The data set is only
parsed once as it's loaded from the input file so the efficiency is high.
"""

print(len([value for line in open("input") for value in line.strip().split("|")[1].split() if len(value) in [2, 3, 4, 7]]))