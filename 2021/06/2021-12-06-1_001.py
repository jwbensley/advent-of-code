"""
Lines of code: 
Readability: 
Efficiency: 


3,4,3,1,2
"""

fish_days = list(map(int, [line.strip().split(",") for line in open("input")][0]))

for i in range(0, 80):
    additions = 0
    for idx, fish_day in enumerate(fish_days):
        if fish_day == 0:
            fish_days[idx] = 6
            additions += 1
        else:
            fish_days[idx] -= 1
    for j in range(0, additions):
        fish_days.append(8)

print(len(fish_days))