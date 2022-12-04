all_values, total = [(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]), int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1])) for line in open("input", "r").read().strip().split("\n")], 0
for values in all_values:
    if values[0] in range(values[2], values[3] + 1) or values[1] in range(values[2], values[3] + 1) or values[2] in range(values[0], values[1] + 1) or values[3] in range(values[0], values[1] + 1): total += 1
print(total)