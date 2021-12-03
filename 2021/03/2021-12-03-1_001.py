"""
Lines of code: medium
Readability: medium
Efficiency: medium

Initial naive version.
30 lines of code, a non excessive amount.
Readability is good apart from the last line which is bad.
The data set is only walked once, but int(strip()) is called n*12 times.
"""

no_of_ones = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0}
lines = 0

for line in open("input"):

    lines += 1
    no_of_ones["0"] += int(line.strip()[0])
    no_of_ones["1"] += int(line.strip()[1])
    no_of_ones["2"] += int(line.strip()[2])
    no_of_ones["3"] += int(line.strip()[3])
    no_of_ones["4"] += int(line.strip()[4])
    no_of_ones["5"] += int(line.strip()[5])
    no_of_ones["6"] += int(line.strip()[6])
    no_of_ones["7"] += int(line.strip()[7])
    no_of_ones["8"] += int(line.strip()[8])
    no_of_ones["9"] += int(line.strip()[9])
    no_of_ones["10"] += int(line.strip()[10])
    no_of_ones["11"] += int(line.strip()[11])

gamma_b = ''.join([
    str(int(not bool((lines / 2) // no_of_ones["0"]))),
    str(int(not bool((lines / 2) // no_of_ones["1"]))),
    str(int(not bool((lines / 2) // no_of_ones["2"]))),
    str(int(not bool((lines / 2) // no_of_ones["3"]))),
    str(int(not bool((lines / 2) // no_of_ones["4"]))),
    str(int(not bool((lines / 2) // no_of_ones["5"]))),
    str(int(not bool((lines / 2) // no_of_ones["6"]))),
    str(int(not bool((lines / 2) // no_of_ones["7"]))),
    str(int(not bool((lines / 2) // no_of_ones["8"]))),
    str(int(not bool((lines / 2) // no_of_ones["9"]))),
    str(int(not bool((lines / 2) // no_of_ones["10"]))),
    str(int(not bool((lines / 2) // no_of_ones["11"])))
    ])

#print epsilon. Need to mask off prefix "0b" with [2:]
#print(int(bin(~int(gamma_b, 2) & 0xFFF)[2:],2))
print(f"{int(gamma_b, 2) * int(bin(~int(gamma_b, 2) & 0xFFF)[2:],2)}")