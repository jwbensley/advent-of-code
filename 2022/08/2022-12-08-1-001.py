lines = open("input").readlines()
grid = []
for line in lines:
    grid.append([x for x in line.strip()])

visible_count = 0
for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        visible = False
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            row_inc, col_inc = direction
            if row_inc == 0 and col_inc == 0: continue
            visible = False
            temp_row = row + row_inc
            temp_col = col + col_inc
            while grid[temp_row][temp_col] < grid[row][col]:
                temp_row += row_inc
                temp_col += col_inc
                if (temp_row < 0 or
                    temp_row > (len(grid) - 1) or
                    temp_col < 0 or
                    temp_col > (len(grid[0]) - 1)):
                    visible = True
                    break
            if visible:
                break
        if visible:
            print(f"{row},{col} is visible")
            visible_count += 1
        else:
            print(f"{row},{col} is not visible")
visible_count += (2 * len(grid))
visible_count += (2 * len(grid[0])) - 4
for row in grid:
    print(row)
print(visible_count)
