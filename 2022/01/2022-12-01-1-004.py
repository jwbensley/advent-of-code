elves, total = [], 0
for line in open("input", "r"):
    if line == "\n": elves.append(total) or (total := 0)
    if line != "\n": total += int(line.strip())
print(sorted(elves)[-1])