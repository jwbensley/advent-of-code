priorities, total = {}, 0
for i in range(97, 123):
    priorities[chr(i)] = i - 96
for i in range(65, 91):
    priorities[chr(i)] = i - 38
for line in open("input", "r"):
    total += priorities[[l for l in line[:(len(line)//2)].strip() if l in line[(len(line)//2):].strip()][0]]
print(total)