#!/usr/local/bin/python3

"""
# Input data comes from: https://adventofcode.com/2019/day/6/input
"""


import sys


def build_tree(orbits):
    """
    Return a tree(dict) of the parent/child orbits
    """

    orbit_tree = {"COM": None}

    for obj in orbits:
        parent = obj.split(")")[0]
        child = obj.split(")")[1]

        if child not in orbit_tree:
            orbit_tree[child] = parent

    return orbit_tree


def get_path_to_root(key, orbit_tree):
    """
    Return the path from leaf (key) back to the tree root
    """

    path = []

    while True:
        path.append(key)
        if orbit_tree[key]:
            key = orbit_tree[key]
        else:
            break

    return path


def orbit_count(count, key, orbit_tree):
    """
    Return the path length from leaf (key) to tree root
    """

    if orbit_tree[key]:
        count = orbit_count((count + 1), orbit_tree[key], orbit_tree)
        return count
    else:
        return count


def print_hops(orbit_tree, src, dst):
    """
    Print the closest shared parent of the two leafs (src, dst)
    """

    src_path = get_path_to_root(src, orbit_tree)
    dst_path = get_path_to_root(dst, orbit_tree)

    shared_parents = [p for p in src_path if p in dst_path]

    closest_parent = None
    closest_distance = sys.maxsize

    for shared_parent in shared_parents:
        src_dist_to_parent = src_path.index(shared_parent) - 1
        dst_dist_to_parent = dst_path.index(shared_parent) - 1
        total_dist = src_dist_to_parent + dst_dist_to_parent
        if total_dist < closest_distance:
            closest_parent = shared_parent
            closest_distance = total_dist

    if closest_parent:
        print(
            "Closest shared parent for {} and {}: {}, total distance {}".format(
                src, dst, closest_parent, closest_distance
            )
        )
        return False
    else:
        return False


def print_orbit_count(orbit_tree):
    """
    Prints the count of each orbit type, from all orbits
    """

    all_orbits = 0
    for key in orbit_tree:
        if orbit_tree[key]:
            all_orbits += orbit_count(0, key, orbit_tree)

    direct_orbits = len(orbit_tree) - 1
    indirect_orbits = all_orbits - direct_orbits
    print(
        "All orbits: {}, direct orbits {}, indirect orbits {}".format(
            all_orbits, direct_orbits, indirect_orbits
        )
    )

    return True


def load_orbits_from_file():
    """
    Returns orbits as a list of strings
    """

    try:
        with open("input", "r") as f:
            orbits = [orbit.strip("\n") for orbit in f.readlines()]
    except Exception as e:
        print("Error while reading input file: {}".format(e))
        return False

    return orbits


def main():

    # The first two are the test cases
    # orbits = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
    # orbits = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
    orbits = load_orbits_from_file()
    if not orbits:
        return False

    orbit_tree = build_tree(orbits)
    if not orbit_tree:
        return False

    if not print_orbit_count(orbit_tree):
        return False

    if not print_hops(orbit_tree, "YOU", "SAN"):
        return False

    return True


if __name__ == "__main__":
    sys.exit(main())
