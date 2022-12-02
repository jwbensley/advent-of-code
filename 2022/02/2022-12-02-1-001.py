results, points, total = {"win": ["C X", "A Y", "B Z"], "draw": ["A X", "B Y", "C Z"], "lose": ["B X", "C Y", "A Z"]}, {"X": 1, "Y": 2, "Z": 3}, 0
for line in open("input", "r"):
    if line.strip() in results["win"]: total += points[line.split()[1]] + 6
    if line.strip() in results["draw"]: total += points[line.split()[1]] + 3
    if line.strip() in results["lose"]: total += points[line.split()[1]]
print(total)