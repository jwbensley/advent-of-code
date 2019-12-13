#!/usr/local/bin/python3

"""
# Input data comes from: https://adventofcode.com/2019/day/5/input
"""


import sys


def execute(intcode):

    # Expect a list of integer opcodes
    for i in intcode:
        assert(isinstance(i, int))

    skip = 0
    ip = 0
    while ip < len(intcode):
        opcode = int(str(intcode[ip])[-2:])

        """
        Parameter modes:
        
        The opcode is a two-digit number based only on the ones and tens digit 
        of the value in an instruction.
        
        The first parameter's mode is in the hundreds digit, the second 
        parameter's mode is in the thousands digit, the third parameter's mode 
        is in the ten-thousands digit, and so on. Any missing modes are 0.

        0 = position/pointer mode
        1 = immediate mode

        The instruction pointer should increase by the number of values in the 
        instruction after the instruction finishes.

        Values used by opcodes are integers and can be negative.
        """


        # Skip memory locations based on instruction length after executing
        if skip > 0:
            skip -= 1
            ip += 1
            continue

        
        # Loading zeros are omitted to default to zero
        pmode_1 = 0
        pmode_2 = 0
        pmode_3 = 0   # Parameters that an instruction writes to will never be in immediate mode.
        # ^ May also be missing leading zero
        try:
            pmode_1 = int(str(intcode[ip])[-3:-2])
            pmode_2 = int(str(intcode[ip])[-4:-3])
            pmode_3 = int(str(intcode[ip])[-5:-4])
        except Exception:
            pass

        # Add values 
        if opcode == 1:

            if pmode_1:
                val_1 = intcode[ip+1]
            else:
                val_1 = intcode[intcode[ip+1]]

            if pmode_2:
                val_2 = intcode[ip+2]
            else:
                val_2 = intcode[intcode[ip+2]]

            result = val_1 + val_2


            ############# Write are never in immediate mode
            if pmode_3:
                intcode[ip+3] = result
            else:
                intcode[intcode[ip+3]] = result

            skip = 3
            ip += 1


        # Multiple values
        elif opcode == 2:

            if pmode_1:
                val_1 = intcode[ip+1]
            else:
                val_1 = intcode[intcode[ip+1]]

            if pmode_2:
                val_2 = intcode[ip+2]
            else:
                val_2 = intcode[intcode[ip+2]]

            result = val_1 * val_2

            ############# Write are never in immediate mode
            if pmode_3:
                intcode[ip+3] = result
            else:
                intcode[intcode[ip+3]] = result

            skip = 3
            ip += 1


        # Request an int as input, arg 1 is always a pointer to store input
        elif opcode == 3:

            value = None
            while True:
                try:
                    value = int(input('Input integer: '))
                    break
                except Exception:
                    pass

            intcode[intcode[ip+1]] = value
            skip = 1
            ip += 1


        # Print an int, stored at the location pointed by arg 1
        elif opcode == 4:

            if pmode_1:
                val_1 = intcode[ip+1]
            else:
                val_1 = intcode[intcode[ip+1]]

            print("Output: {}".format(val_1))
            skip = 1
            ip += 1


        # jump-if-true: if (arg1!=0) jump to arg2
        elif opcode == 5:

            if pmode_1:
                val_1 = intcode[ip+1]
            else:
                val_1 = intcode[intcode[ip+1]]

            if pmode_2:
                val_2 = intcode[ip+2]
            else:
                val_2 = intcode[intcode[ip+2]]

            if val_1 != 0:
                ip = val_2
            else:
                skip = 2
                ip += 1


        # jump-if-false: if (arg!=0) jump to arg2
        elif opcode == 6:

            if pmode_1:
                val_1 = intcode[ip+1]
            else:
                val_1 = intcode[intcode[ip+1]]

            if pmode_2:
                val_2 = intcode[ip+2]
            else:
                val_2 = intcode[intcode[ip+2]]

            if val_1 == 0:
                ip = val_2
            else:
                skip = 2
                ip += 1


        # less than: if (arg1<arg2) 1 ?: 0
        elif opcode == 7:

            if pmode_1:
                val_1 = intcode[ip+1]
            else:
                val_1 = intcode[intcode[ip+1]]

            if pmode_2:
                val_2 = intcode[ip+2]
            else:
                val_2 = intcode[intcode[ip+2]]

            if val_1 < val_2:
                intcode[intcode[ip+3]] = 1
            else:
                intcode[intcode[ip+3]] = 0

            skip = 3
            ip += 1


        # equals: if (arg1==arg2) 1 ?: 0
        elif opcode == 8:

            if pmode_1:
                val_1 = intcode[ip+1]
            else:
                val_1 = intcode[intcode[ip+1]]

            if pmode_2:
                val_2 = intcode[ip+2]
            else:
                val_2 = intcode[intcode[ip+2]]

            if val_1 == val_2:
                intcode[intcode[ip+3]] = 1
            else:
                intcode[intcode[ip+3]] = 0

            skip = 3
            ip += 1


        # Halt
        elif opcode == 99:
            return True

        # HCF
        else:
            print("Unknown instruction {} at index {}".format(opcode, ip))
            return False

    print("Reached default return statement!")
    return False

"""
Return intcode as a list of integers
"""
def load_intructs_from_file():

    try:
        with open('input', 'r') as f:
            line = f.readline().strip("\n")
            intcode = [int(i) for i in line.split(",")]
    except Exception as e:
        print("Error while reading input file: {}".format(e))
        return False

    return intcode


def main():


    # The first three are the test cases
    #intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    #intcode = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    #intcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    intcode = load_intructs_from_file()
    if not intcode:
        return False

    if not execute(intcode[:]):
        return False

    if not execute(intcode[:]):
        return False


    return True


if __name__ == "__main__":
    sys.exit(main())
