#!/usr/local/bin/python3

"""
# Input data comes from: https://adventofcode.com/2019/day/2/input
"""


import sys


def execute(instructions):

    skip = 0
    for i,v in enumerate(instructions):

        # Skip over memory locations based on the number of args an opcode has
        if skip > 0:
            skip -= 1
            continue

        # Add args pointed by 1 and 2 and write to location pointed by 3
        if v == 1:
            instructions[instructions[i+3]] = (instructions[instructions[i+1]] + instructions[instructions[i+2]])
            skip = 3
        # Multiple args pointed by 1 and 2 and write to location pointed by 3
        elif v == 2:
            instructions[instructions[i+3]] = (instructions[instructions[i+1]] * instructions[instructions[i+2]])
            skip = 3
        # Halt
        elif v == 99:
            return instructions
        # HCF
        else:
            print("Unknown instruction {} at index {}".format(v,i))
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
                    return n,v

    return False, False


def load_intructs_from_file():

    try:
        with open('input') as f:
            line = f.readline().strip("\n")
            orig_instructs = [int(i) for i in line.split(",")]
    except Exception as e:
        print("Error while reading input file: {}".format(e))
        return False

    return orig_instructs


def restore_instructs(orig_instructs):

    orig_instructs[1] = 12
    orig_instructs[2] = 2

    return orig_instructs


def main():

    orig_instructs = load_intructs_from_file()
    if not orig_instructs:
        return False


    # Pass a copy of orig_instructs[] so that it isn't modified in-place
    restored_instructs = restore_instructs(orig_instructs[:])


    exec_instructs = execute(restored_instructs[:])
    if not exec_instructs:
        return False
    print("Executed instruction set: {}\n".format(exec_instructs))


    noun, verb = find_19690720(restored_instructs[:])
    if not noun:
        return False
    else:
        print("Found 19690720 with noun {}, verb {}".format(noun,verb))

    return True


if __name__ == "__main__":
    sys.exit(main())
