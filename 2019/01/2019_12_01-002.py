#!/usr/local/bin/python3

"""
# Input data comes from: https://adventofcode.com/2019/day/1/input
"""


with open('input') as f:
    input_data = [int(l) for l in f.readlines()]

# Part 1:
mass_fuel_req = sum([int(mass/3)-2 for mass in input_data])

# Part 2:
all_fuel_req = 0

for mass in input_data:
    fuel_req = int(mass/3)-2
    all_fuel_req += fuel_req

    while (fuel_req > 0):
        fuel_overhead = int(fuel_req/3)-2
        if fuel_overhead > 0:
            all_fuel_req += fuel_overhead
        fuel_req = fuel_overhead


print(mass_fuel_req)
print(all_fuel_req)

