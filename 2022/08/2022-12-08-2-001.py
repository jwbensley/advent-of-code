lines = open("input").readlines()
grid = []
for line in lines:
    grid.append([x for x in line.strip()])

highest = 0
for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        scores = []
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            row_inc, col_inc = direction
            if row_inc == 0 and col_inc == 0: continue
            temp_row = row + row_inc
            temp_col = col + col_inc
            print(f"{temp_row},{temp_col} : {row},{col}")
            score = 0
            while (temp_row >= 0 and
                    temp_row <= (len(grid) - 1) and
                    temp_col >= 0 and
                    temp_col <= (len(grid[0]) - 1)):
                if grid[temp_row][temp_col] >= grid[row][col]:
                    score += 1
                    break
                score += 1
                temp_row += row_inc
                temp_col += col_inc
            scores.append(score) 
            print(f"{row},{col} score: {scores}")
        x = scores[0]
        for s in scores[1:]:
            x = x * s
        if x > highest:
            print(f"{row},{col} is new high score: {x}")
            highest = x
        else:
            print(f"{row},{col} is not a high score: {x}")

for row in grid:
    print(row)
print(highest)
