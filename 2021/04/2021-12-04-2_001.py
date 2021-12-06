"""
Lines of code: high
Readability: medium
Efficiency: low

Initial naive version.
Simply aweful.
"""

def find_last_block():
    block_ids = list(range(0, len(blocks)-1))

    for call in calls:
        for block in blocks:
            for row in blocks[block]["rows"]:
                if call in blocks[block]["rows"][row]:
                    if not blocks[block]["rows"][row][call]:
                        blocks[block]["rows"][row][call] = True
                        count = 0
                        for num in blocks[block]["rows"][row]:
                            if blocks[block]["rows"][row][num]:
                                count += 1
                        if count == 5:
                            winning_block = block
                            winning_number = int(call)
                            print(f"winning_block: {winning_block}, winning_number: {winning_number}")
                            print(f"Row {row}: {blocks[block]['rows'][row]}")
                            if block in block_ids:
                                block_ids.remove(block)
                                if len(block_ids) == 0:
                                    print(f"Last winning block ID was {winning_block}")
                                    return winning_block, winning_number

            for col in blocks[block]["cols"]:
                if call in blocks[block]["cols"][col]:
                    if not blocks[block]["cols"][col][call]:
                        blocks[block]["cols"][col][call] = True
                        count = 0
                        for num in blocks[block]["cols"][col]:
                            if blocks[block]["cols"][col][num]:
                                count += 1
                        if count == 5:
                            winning_block = block
                            winning_number = int(call)
                            print(f"winning_block: {winning_block}, winning_number: {winning_number}")
                            print(f"Col {col}: {blocks[block]['cols'][col]}")
                            if block in block_ids:
                                block_ids.remove(block)
                                if len(block_ids) == 0:
                                    print(f"Last winning block ID was {winning_block}")
                                    return winning_block, winning_number

calls = None
start_of_block = False
blocks = {}
block_idx = 0
row_idx = 0
col_idx = 0

for line in open("input"):

    if not calls:
        calls = line.strip().split(",")

    if line == "\n":
        start_of_block = True
        blocks[block_idx] = {
            "rows": {
                0: {},
                1: {},
                2: {},
                3: {},
                4: {},
            },
            "cols": {
                0: {},
                1: {},
                2: {},
                3: {},
                4: {},
            }
        }
        continue

    elif start_of_block:
        blocks[block_idx]["rows"][row_idx] = {
            line.strip().split()[0]: False,
            line.strip().split()[1]: False,
            line.strip().split()[2]: False,
            line.strip().split()[3]: False,
            line.strip().split()[4]: False,
        }
        blocks[block_idx]["cols"][0][line.strip().split()[0]] = False
        blocks[block_idx]["cols"][1][line.strip().split()[1]] = False
        blocks[block_idx]["cols"][2][line.strip().split()[2]] = False
        blocks[block_idx]["cols"][3][line.strip().split()[3]] = False
        blocks[block_idx]["cols"][4][line.strip().split()[4]] = False
        row_idx += 1
        if row_idx == 5:
            start_of_block = False
            row_idx = 0
            block_idx += 1


winning_block, winning_number = find_last_block()

total = 0
for row in blocks[winning_block]["rows"]:
    for num in blocks[winning_block]["rows"][row]:
        if not blocks[winning_block]["rows"][row][num]:
            total += int(num)

print(f"{total*winning_number}")