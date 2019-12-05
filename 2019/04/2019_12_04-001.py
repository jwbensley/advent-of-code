#!/usr/local/bin/python3

"""
# Input data: 307237-769058
"""


import sys



def has_consecutive(num):

    num = str(num)

    for i in range(0, len(num)-1):
        if (num[i] == num[i+1]):
            return True

    return False



def never_decreases(num):

    num = str(num)

    for i in range(0, len(num)-1):
        if (int(num[i]) > int(num[i+1])):
            return False

    if (int(num[len(num)-2]) > int(num[len(num)-1])):
        return False

    return True


def has_pair(num):

    num = str(num)

    for i in range(0, len(num)-2):
        if ((num[i] == num[i+1]) and (num[i] != num[i+2])):
            if i > 0:
                if (num[i] != num[i-1]):
                    return True
            else:
                return True

    if ((num[3] != num[4]) and (num[4] == num[5])):
        return True

    return False


def main():

    count1 = 0
    count2 = 0

    for i in range (307237, 769058+1):

        if not has_consecutive(i):
            continue

        if not never_decreases(i):
            continue

        count1 += 1

        if not has_pair(i):
            continue

        count2 +=1


    print("Total conforming numbers, part 1: {}".format(count1))
    print("Total conforming numbers, part 2: {}".format(count2))

    return True


if __name__ == "__main__":
    sys.exit(main())
