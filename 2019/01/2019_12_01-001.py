#!/usr/local/bin/python3

"""
Requirements:
sudo -H pip3 install requests

# Input data comes from: https://adventofcode.com/2019/day/1/input
"""


import requests
import sys


def get_data_file():

    with open('input') as f:
        # No need for: int(l.strip("\n"))
        # int() will implicitly remove the new line
        lines = [int(l) for l in f.readlines()]

    return lines

"""
def get_data_http():

    try:
        req = requests.get(
            url="https://adventofcode.com/2019/day/1/input"
        )
    except requests.exceptions.SSLError as e:
        print("SSL error when fetching API data:\n{}".format(e))
        return False

    if req.status_code is not requests.codes.ok:
        print("GET failed, result code was:\n{}".format(req.status_code))
        print(req.text)
        return False

    return req.text
"""

"""
def data_to_list(raw_data):

    print(raw_data)

    return False

    return raw_data
"""

def return_data_from_file():

    raw_data = get_data_file()
    if not raw_data:
        return False

    return raw_data

"""
def return_data_from_http():

    raw_data = get_data_http()
    if not raw_data:
        return False

    input_data = data_to_list(raw_data)
    if not input_data:
        return False

    return input_data
"""

def fuel_for_all(input_data):

    total_fuel = 0

    for mass in input_data:
        # int() implicitly rounds down
        mass_fuel = int(mass/3)-2
        total_fuel += mass_fuel

        while (mass_fuel > 0):
            mass_fuel_overhead = int(mass_fuel/3)-2
            if mass_fuel_overhead > 0:
                total_fuel += mass_fuel_overhead
            mass_fuel = mass_fuel_overhead

    return total_fuel

def fuel_for_mass(input_data):

    """
    total_mass_fuel = 0

    for mass in input_data:
        fuel = int(mass/3)-2
        total_mass_fuel += fuel
    """
    
    total_mass_fuel = sum([int(mass/3)-2 for mass in input_data])

    return total_mass_fuel


def main():

    #input_data = return_data_from_http()
    input_data = return_data_from_file()
    if not input_data:
        return False

    mass_fuel_req = fuel_for_mass(input_data)
    print(mass_fuel_req)
    all_fuel_req = fuel_for_all(input_data)
    print(all_fuel_req)

    return True


if __name__ == "__main__":
    sys.exit(main())
