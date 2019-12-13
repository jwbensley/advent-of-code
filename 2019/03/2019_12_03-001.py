#!/usr/local/bin/python3

"""
# Input data comes from: https://adventofcode.com/2019/day/3/input
"""


import sys


def build_wire_map(wire_coords):

    wire_map = {}
    wire_x = 0
    wire_y = 0
    steps = 0
    
    for coord in wire_coords:
        i = int(coord[1:])
        while i > 0:

            if coord[0] == "D":
                wire_y -= 1
                steps += 1
            elif coord[0] == "L":
                wire_x -= 1
                steps += 1
            elif coord[0] == "U":
                wire_y += 1
                steps += 1
            elif coord[0] == "R":
                wire_x += 1
                steps += 1
            else:
                print("Unknown coord: {}".format(coord))
                return False

            wire_map[str(wire_x)+","+str(wire_y)] = steps
            i -= 1

    return wire_map


def get_intersections(wire_data, wire_map):

    wire_x = 0
    wire_y = 0
    steps = 0
    closest_distance = sys.maxsize
    closest_dist_coords = "0,0"
    closest_steps = sys.maxsize
    closest_steps_coords = "0,0"

    for coord in wire_data:
        i = int(coord[1:])
        while i > 0:

            if coord[0] == "D":
                wire_y -= 1
                steps += 1
            elif coord[0] == "L":
                wire_x -= 1
                steps += 1
            elif coord[0] == "U":
                wire_y += 1
                steps += 1
            elif coord[0] == "R":
                wire_x += 1
                steps += 1
            else:
                print("Unknown coord: {}".format(coord))
                return False

            if (str(wire_x)+","+str(wire_y)) in wire_map:
                distance = (abs(0 - wire_x) + abs(0 - wire_y))
                total_steps = (steps + wire_map[str(wire_x)+","+str(wire_y)])
                if distance < closest_distance:
                    closest_distance = distance
                    closest_dist_coords = (str(wire_x)+","+str(wire_y))
                if total_steps < closest_steps:
                    closest_steps = total_steps
                    closest_steps_coords = (str(wire_x)+","+str(wire_y))
            i -= 1

    print("Closest by distance is {}, distance is {}".format(closest_dist_coords, closest_distance))
    print("Closest by steps is {}, steps is {}".format(closest_steps_coords, closest_steps))
    
    return True


def load_wire_data():

    try:
        with open('input') as f:
            lines = [str(l).strip("\n").split(",") for l in f.readlines()]
    except Exception as e:
        print("Couldn't read input file: {}".format(e))
        return False

    return lines


def main():


    #wire_data = ['R8,U5,L5,D3'.split(","),'U7,R6,D4,L4'.split(",")]
    # Closest intersection by distance is: 6
    # Closest intersection by steps is: 

    #wire_data = ['R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(","),
    #             'U62,R66,U55,R34,D71,R55,D58,R83'.split(",")]
    # Closest intersection by distance is: 159
    # Closest intersection by steps is: 610

    #wire_data = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(","),
    #             'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(",")]
    # Closest intersection by distance is: 135
    # Closest intersection by steps is: 410

    wire_data = load_wire_data()
    if not wire_data:
        return False

    wire_0_map = build_wire_map(wire_data[0])
    if not wire_0_map:
        return False

    intersections = get_intersections(wire_data[1], wire_0_map)
    if not intersections:
        return False

    # Closest intersection by distance is: 209
    # Closest intersection by steps is: 43258

    return True


if __name__ == "__main__":
    sys.exit(main())
