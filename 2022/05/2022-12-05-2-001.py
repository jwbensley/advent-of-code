p = [["D", "T", "R", "B", "J", "L", "W", "G"],["S", "W", "C"],["R", "Z", "T", "M"],["D", "T", "C", "H", "S", "P", "V"],["G", "P", "T", "L", "D", "Z"],["F", "B", "R", "Z", "J", "Q", "C", "D"],["S", "B", "D", "J", "M", "F", "T", "R"],["L", "H", "R", "B", "T", "V", "M"],["Q", "P", "D", "S", "V"]]
for line in open("input", "r"):
    if line[:4] != "move": continue
    p[int(line.split()[5])-1].extend(p[int(line.split()[3])-1][-int(line.split()[1]):])
    p[int(line.split()[3])-1] = p[int(line.split()[3])-1][:-int(line.split()[1])]
for x in p: print(x[-1], end="")