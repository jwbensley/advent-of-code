with open("input", "r") as f:
    elves = [sum(list(map(int, elv.strip().split("\n")))) for elv in f.read().split("\n\n")]
print(sum(sorted(elves)[-3:]))