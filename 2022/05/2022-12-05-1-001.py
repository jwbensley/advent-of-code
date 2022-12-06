p = [["D", "T", "R", "B", "J", "L", "W", "G"],["S", "W", "C"],["R", "Z", "T", "M"],["D", "T", "C", "H", "S", "P", "V"],["G", "P", "T", "L", "D", "Z"],["F", "B", "R", "Z", "J", "Q", "C", "D"],["S", "B", "D", "J", "M", "F", "T", "R"],["L", "H", "R", "B", "T", "V", "M"],["Q", "P", "D", "S", "V"]]
for line in open("input", "r"):
    if line[:4] != "move": continue
    for i in range(1, int(line.split()[1])+1): p[int(line.split()[5])-1].append(p[int(line.split()[3])-1].pop())
for x in p: print(x[-1], end="")