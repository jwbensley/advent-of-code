elves, total = [], 0
for line in open("input", "r"):
    total += int(line.strip()) if line.strip() else 0
    if line == "\n":
        elves.append(total)
        total = 0  
print(sorted(elves)[-1])