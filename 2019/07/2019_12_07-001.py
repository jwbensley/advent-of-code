#!/usr/local/bin/python3

"""
# Input data comes from: https://adventofcode.com/2019/day/7/input
"""


import sys



def execute(intcode, input1, input2):

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

            if input1 != None:
                ##print("Using phase setting: {}".format(input1))
                intcode[intcode[ip+1]] = input1
                input1 = None
            else:
                ##print("Using signal: {}".format(input2))
                intcode[intcode[ip+1]] = input2
            skip = 1
            ip += 1


        # Print an int, stored at the location pointed by arg 1
        elif opcode == 4:

            if pmode_1:
                val_1 = intcode[ip+1]
            else:
                val_1 = intcode[intcode[ip+1]]

            ##print("Output: {}".format(val_1))
            return(val_1)
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


def execute2(intcode, ip, input1, input2):
    """
    Execute intcode (a list of integers) and return opcode 4 result
    """

    ##print("Signal: {}, IP: {}".format(input2, ip))

    # Expect a list of integer opcodes
    for i in intcode:
        assert(isinstance(i, int))

    skip = 0
    #ip = 0
    ret_val = None
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

        ##print("Exec {} at {}".format(opcode, ip))

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

            """
            value = None
            while True:
                try:
                    value = int(input('Input integer: '))
                    break
                except Exception:
                    pass

            intcode[intcode[ip+1]] = value
            """
            if input1 != None:
                ##print("Using phase setting: {}".format(input1))
                intcode[intcode[ip+1]] = input1
                input1 = None
            else:
                ##print("Using signal: {}".format(input2))
                intcode[intcode[ip+1]] = input2
            skip = 1
            ip += 1


        # Print an int, stored at the location pointed by arg 1
        elif opcode == 4:

            if pmode_1:
                val_1 = intcode[ip+1]
            else:
                val_1 = intcode[intcode[ip+1]]

            #print("Output: {}".format(val_1))
            ret_val = val_1
            ##print("executed: {}".format(intcode))
            return ret_val, ip
            #skip = 1
            #ip += 1


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
            return None,None

        # HCF
        else:
            print("Unknown instruction {} at index {}".format(opcode, ip))
            return sys.maxsize,sys.maxsize

    print("Reached default return statement!")
    return sys.maxsize,sys.maxsize


def find_max(intcode, phase_min, phase_max):

    initial_signal = 0
    max_signal = 0
    max_phase = []

    for a in range(phase_min, phase_max):
       for b in range(phase_min, phase_max):
          for c in range(phase_min, phase_max):
             for d in range(phase_min, phase_max):
                for e in range(phase_min, phase_max):

                    # Each phase can only occur once in the sequence
                    if len(set([a, b, c, d, e])) != 5:
                       continue

                    amp1_phase = a
                    amp1_signal = initial_signal

                    amp2_phase = b
                    amp2_signal = execute(intcode, amp1_phase, amp1_signal)
                    if amp2_signal == None:
                        return False

                    amp3_phase = c
                    amp3_signal = execute(intcode, amp2_phase, amp2_signal)
                    if amp3_signal == None:
                        return False

                    amp4_phase = d
                    amp4_signal = execute(intcode, amp3_phase, amp3_signal)
                    if amp4_signal == None:
                        return False

                    amp5_phase = e
                    amp5_signal = execute(intcode, amp4_phase, amp4_signal)
                    if amp5_signal == None:
                        return False

                    thrust_signal = execute(intcode, amp5_phase, amp5_signal)
                    if thrust_signal == None:
                        return False

                    if thrust_signal > max_signal:
                       max_signal = thrust_signal
                       max_phase = [a, b, c, d, e]

    return max_signal, max_phase


def find_max_2(intcode, phase_min, phase_max):

    initial_signal = 0
    max_signal = 0
    max_phase = []
    
    """
    for a in range(9, 10):
       for b in range(8, 9):
          for c in range(7, 8):
             for d in range(6, 7):
                for e in range(5, 6):
    """

    for a in range(phase_min, phase_max):
       for b in range(phase_min, phase_max):
          for c in range(phase_min, phase_max):
             for d in range(phase_min, phase_max):
                for e in range(phase_min, phase_max):

                    # Each phase can only occur once in the sequence
                    if len(set([a, b, c, d, e])) != 5:
                        continue


                    amp1_phase = a
                    amp2_phase = b
                    amp3_phase = c
                    amp4_phase = d
                    amp5_phase = e
                    amp1_intcode = intcode[:]
                    amp1_ip = 0
                    amp2_intcode = intcode[:]
                    amp2_ip = 0
                    amp3_intcode = intcode[:]
                    amp3_ip = 0
                    amp4_intcode = intcode[:]
                    amp4_ip = 0
                    amp5_intcode = intcode[:]
                    amp5_ip = 0

                    ##print("Using: {}, {}".format([a, b, c, d, e], initial_signal))

                    amp1_signal = initial_signal
                    while True:


                        ##print("intcode1: {}".format(amp1_intcode))
                        amp2_signal, amp1_ip = execute2(amp1_intcode, amp1_ip, amp1_phase, amp1_signal)
                        ##print("Got: {}, {}".format(amp2_signal, amp1_ip))
                        amp1_phase = None
                        if amp2_signal == None:
                            ##print("None1")
                            pass
                        else:
                            amp1_ip += 2
                        if amp2_signal == sys.maxsize:
                            ##print("Fucked1")
                            pass
                            return False
                        ##print("\n")

                        ##print("intcode2: {}".format(amp2_intcode))
                        amp3_signal, amp2_ip = execute2(amp2_intcode, amp2_ip, amp2_phase, amp2_signal)
                        ##print("Got: {}, {}".format(amp3_signal, amp2_ip))
                        amp2_phase = None
                        if amp3_signal == None:
                            pass
                            ##print("None2")
                        else:
                            amp2_ip += 2
                        if amp3_signal == sys.maxsize:
                            ##print("Fucked2")
                            pass
                            return False
                        ##print("\n")

                        ##print("intcode3: {}".format(amp3_intcode))
                        amp4_signal, amp3_ip = execute2(amp3_intcode, amp3_ip, amp3_phase, amp3_signal)
                        ##print("Got: {}, {}".format(amp4_signal, amp3_ip))
                        amp3_phase = None
                        if amp4_signal == None:
                            ##print("None3")
                            pass
                        else:
                            amp3_ip += 2
                        if amp4_signal == sys.maxsize:
                            ##print("Fucked3")
                            pass
                            return False
                        ##print("\n")

                        ##print("intcode4: {}".format(amp4_intcode))
                        amp5_signal, amp4_ip = execute2(amp4_intcode, amp4_ip, amp4_phase, amp4_signal)
                        ##print("Got: {}, {}".format(amp5_signal, amp4_ip))
                        amp4_phase = None
                        if amp5_signal == None:
                            ##print("None4")
                            pass
                        else:
                            amp4_ip += 2
                        if amp5_signal == sys.maxsize:
                            ##print("Fucked4")
                            return False
                        ##print("\n")

                        ##print("intcode5: {}".format(amp5_intcode))
                        amp1_signal, amp5_ip = execute2(amp5_intcode, amp5_ip, amp5_phase, amp5_signal)
                        ##print("Got: {}, {}".format(amp1_signal, amp5_ip))
                        amp5_phase = None
                        if amp1_signal == None:
                            ##print("None5")
                            break
                        else:
                            amp5_ip += 2
                        if amp1_signal == sys.maxsize:
                            ##print("Fucked5")
                            return False
                        ##print("\n")

                        if amp1_signal > max_signal:
                            max_signal = amp1_signal
                            max_phase = [a, b, c, d, e]
                            #print("New max signal is {} from phases: {}".format(max_signal, max_phase))
                        else:
                            pass
                            ##print("Less than max signal {} from phases: {}".format(max_signal, max_phase))
                        ##print(" \n")


    return max_signal, max_phase


def load_intructs_from_file():
    """
    Return intcode as a list of integers
    """

    try:
        with open('input', 'r') as f:
            line = f.readline().strip("\n")
            intcode = [int(i) for i in line.split(",")]
    except Exception as e:
        print("Error while reading input file: {}".format(e))
        return False

    return intcode


def main():

    # These first three are part 1 test cases:
    #intcode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    # Max signal is 43210 from phases: [4, 3, 2, 1, 0]
    #intcode = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    # Max signal is 54321 from phases: [0, 1, 2, 3, 4]
    #intcode = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    # Max signal is 65210 from phases: [1, 0, 4, 3, 2]
    intcode = load_intructs_from_file()
    if not intcode:
        return False
    # Max signal is 262086 from phases: [2, 1, 4, 0, 3]

    max_signal, max_phase = find_max(intcode, 0, 5)
    if not max_signal:
        return False
    print("Max signal is {} from phases: {}".format(max_signal, max_phase))


    # These next two are part 2 test cases:
    #intcode = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    # Max signal is 139629729 from phases: [9, 8, 7, 6, 5]
    #intcode = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    # Max signal is 18216 from phases: [9, 7, 8, 5, 6]
    intcode = load_intructs_from_file()
    # Max signal is 5371621 from phases: [5, 7, 6, 8, 9]
    if not intcode:
        return False

    max_signal, max_phase = find_max_2(intcode, 5, 10)
    if not max_signal:
        print("FuckedRoot: {}".format(max_signal))
        return False
    print("Max signal is {} from phases: {}".format(max_signal, max_phase))

    return True


if __name__ == "__main__":
    sys.exit(main())
