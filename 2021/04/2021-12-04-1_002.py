"""
Lines of code: medium
Readability: medium
Efficiency: medium

35 lines of code. Can't write much less code without dropping readability.
Readability is medium, it's not too condensed.
Parse the input file only once, and walk the list of bingo calls only once,
but walk all blocks for every bingo call. Not super efficient but "OK".
"""

calls = None
blocks = []

for line in open("input"):
    if not calls:
        calls = line.strip().split(",")

    elif line == "\n":
        blocks.append([])

    else:
        blocks[-1].append(line.strip().split()[0])
        blocks[-1].append(line.strip().split()[1])
        blocks[-1].append(line.strip().split()[2])
        blocks[-1].append(line.strip().split()[3])
        blocks[-1].append(line.strip().split()[4])

called = []
for call in calls:
    called.append(call)

    for idx, block in enumerate(blocks):
        x = 0
        for y in range(0, 25, 5):
            if (
                    block[y] in called and
                    block[y + 1] in called and
                    block[y + 2] in called and
                    block[y + 3] in called and
                    block[y + 4] in called
                ) or (
                    block[x] in called and
                    block[x + 5] in called and
                    block[x + 10] in called and
                    block[x + 15] in called and
                    block[x + 20] in called
                ):
                print(sum([int(num) for num in block if num not in called]) * int(call))
                exit(0)
            x += 1