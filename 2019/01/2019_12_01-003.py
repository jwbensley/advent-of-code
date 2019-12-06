#!/usr/local/bin/python3

"""
# Input data comes from: https://adventofcode.com/2019/day/1/input
"""

with open('input', 'r') as f:
    
    part_1 = []
    part_2 = []

    for line in f:
        mass = int(line.rstrip())
        # int() implicitly rounds down
        fuel = int(mass/3)-2
        part_1.append(fuel)

        while (fuel > 0):
            fuel_overhead = int(fuel/3)-2
            if fuel_overhead > 0:
                part_2.append(fuel)
            fuel = fuel_overhead


print("{}".format(sum(part_1)))
print("{}".format(sum(part_1)+sum(part_2)))
