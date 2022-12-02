play = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
total = 0
for line in open("input", "r"):
    total += play[line.strip()]
print(total)