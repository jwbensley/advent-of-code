#!/usr/local/bin/python3

"""
# Input data comes from: https://adventofcode.com/2019/day/8/input
"""


import sys


def find_fewest_zeros(pixels, width, height):
    """
    Return the sum of the frequency of 1's multiplied by the frequency of 2's
    in the layer with the fewest zeros.
    """

    fewest_zeros = sys.maxsize
    multiple = 0

    for i in range(0, (len(pixels) // (width * height)) + 1):

        start = i * (width * height)
        end = (i + 1) * (width * height)
        layer = pixels[start:end]

        num_0 = len([zero for zero in layer if zero == 0])
        num_1 = len([one for one in layer if one == 1])
        num_2 = len([two for two in layer if two == 2])

        if (num_0 <= fewest_zeros) and (num_0):
            fewest_zeros = num_0
            result = layer[:]
            multiple = num_1 * num_2

        i += width * height

    print("Sum of '1' frequency * '2' frequency: {}".format(multiple))
    return multiple


def load_pixels_from_file(width, height):
    """
    Return pixels as a list of integers
    """

    try:
        with open("input", "r") as f:
            line = f.readline().strip("\n")
            pixels = [int(i) for i in line]
    except Exception as e:
        print("Error while reading input file: {}".format(e))
        return False

    # Ensure the picture has the correct number of layers given the dimensions
    if len(pixels) % (width * height) != 0:
        print("Pixel data has the wrong dimensions")
        return False

    return pixels


def main():

    # "The image you received is 25 pixels wide and 6 pixels tall."
    pixels = load_pixels_from_file(25, 6)
    if not pixels:
        return 1

    layer = find_fewest_zeros(pixels, 25, 6)
    if not layer:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
