elves, total = [], 0
for line in open("input", "r"):
    if line == "\n":
        elves.append(total)
        total = 0
    else:
        total += int(line.strip())
print(sorted(elves)[-1])