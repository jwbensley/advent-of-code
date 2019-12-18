#!/usr/local/bin/python3

"""
# Input data comes from: https://adventofcode.com/2019/day/2/input
"""


import sys


def execute(instructs):

    skip = 0
    for i, v in enumerate(instructs):

        # Skip over memory locations based on the number of args an opcode has
        if skip > 0:
            skip -= 1
            continue

        # Add args pointed by 1 and 2 and write to location pointed by 3
        if v == 1:
            instructs[instructs[i + 3]] = (
                instructs[instructs[i + 1]] + instructs[instructs[i + 2]]
            )
            skip = 3
        # Multiple args pointed by 1 and 2 and write to location pointed by 3
        elif v == 2:
            instructs[instructs[i + 3]] = (
                instructs[instructs[i + 1]] * instructs[instructs[i + 2]]
            )
            skip = 3
        # Halt
        elif v == 99:
            return instructs
        # HCF
        else:
            print("Unknown instruction {} at index {}".format(v, i))
            return False

    print("Reached default return statement!")
    return False


def find_19690720(restored_instructs):

    for n in range(99):
        for v in range(99):
            tmp_instructs = restored_instructs[:]
            tmp_instructs[1] = n
            tmp_instructs[2] = v
            result = execute(tmp_instructs)
            if result:
                if result[0] == 19690720:
                    return n, v

    return False, False


def load_intructs_from_file():

    try:
        with open("input", "r") as f:
            line = f.readline().rstrip()
            orig_instructs = [int(i) for i in line.split(",")]
    except Exception as e:
        print("Error while reading input file: {}".format(e))
        return False

    return orig_instructs


def main():

    orig_instructs = load_intructs_from_file()
    if not orig_instructs:
        return 1

    # Restore the instruction to before the crash
    orig_instructs[1] = 12
    orig_instructs[2] = 2

    exec_instructs = execute(orig_instructs[:])
    if not exec_instructs:
        return 1
    print("Executed instruction set: {}\n".format(exec_instructs))

    noun, verb = find_19690720(orig_instructs[:])
    if not noun:
        return 1
    else:
        print("Found 19690720 with noun {}, verb {}".format(noun, verb))

    return 0


if __name__ == "__main__":
    sys.exit(main())
