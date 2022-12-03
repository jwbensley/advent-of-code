total = 0
for line in open("input", "r"):
    line = [int(x) for x in line.replace("A", "1").replace("B", "2").replace("C", "3").replace("X", "1").replace("Y", "2").replace("Z", "3").split()]
    if line[1] == (line[0] + 1) or line[1] == (line[0] - 2): total += line[1] + 6
    if line[1] == line[0]: total += line[1] + 3
    if line[1] == (line[0] - 1) or line[1] == (line[0] + 2): total += line[1]
print(total)