highest, total = 0, 0
for line in open("input", "r"):
    total += int(line.strip()) if line.strip() else 0
    if line == "\n":
        highest, total = total if total > highest else highest, 0  
print(highest)