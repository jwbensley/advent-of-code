#!/usr/local/bin/python3

"""
# Input data comes from: https://adventofcode.com/2019/day/1/input
"""


import sys


def get_data_from_file():

    try:
        with open("input") as f:
            # No need for: int(l.strip("\n"))
            # int() will implicitly remove the new line
            lines = [int(l) for l in f.readlines()]
    except Exception as e:
        print("Couldn't read input file: {}".format(e))
        return False

    return lines


def fuel_for_all(input_data):

    total_fuel = 0

    for mass in input_data:
        # int() implicitly rounds down
        mass_fuel = int(mass / 3) - 2
        total_fuel += mass_fuel

        while mass_fuel > 0:
            mass_fuel_overhead = int(mass_fuel / 3) - 2
            if mass_fuel_overhead > 0:
                total_fuel += mass_fuel_overhead
            mass_fuel = mass_fuel_overhead

    return total_fuel


def fuel_for_mass(input_data):

    total_mass_fuel = sum([int(mass / 3) - 2 for mass in input_data])

    return total_mass_fuel


def main():

    input_data = get_data_from_file()
    if not input_data:
        return 1

    print("Part 1: {}".format(fuel_for_mass(input_data)))
    print("Part 2: {}".format(fuel_for_all(input_data)))

    return 0


if __name__ == "__main__":
    sys.exit(main())
