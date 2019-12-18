#!/usr/local/bin/python3

"""
# Input data comes from: https://adventofcode.com/2019/day/1/input
"""

with open("input", "r") as f:

    part_1 = []
    part_2 = []

    for line in f:
        fuel = int(line.rstrip()) // 3 - 2
        part_1.append(fuel)

        fuel_overhead = (fuel // 3) - 2
        while fuel_overhead > 0:
            part_2.append(fuel_overhead)
            fuel_overhead = (fuel_overhead // 3) - 2

print("Part 1: {}".format(sum(part_1)))
print("Part 2: {}".format(sum(part_1) + sum(part_2)))