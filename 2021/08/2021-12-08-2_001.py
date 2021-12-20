"""
Lines of code: 
Readability: 
Efficiency: 


"""

totals = []
for line in open("input"):
    values = line.strip().replace("|", "").split()

    zero = set()
    one = set()
    two = set()
    three = set()
    four = set()
    five = set()
    six = set()
    seven = set()
    eight = set()
    nine = set()

    for val in values:
        if len(val) == 2:
            for char in val:
                one.add(char)
            print(f"Found one: {one}")
        elif len(val) == 4:
            for char in val:
                four.add(char)
            print(f"Found four: {four}")
        elif len(val) == 3:
            for char in val:
                seven.add(char)
            print(f"Found seven: {seven}")
        elif len(val) == 7:
            for char in val:
                eight.add(char)
            print(f"Found eight: {eight}")

    for val in values:
        if len(val) == 5: # 2/3/5
            tmp = set()
            for char in val:
                tmp.add(char)
            if one.issubset(tmp):
                three = tmp.copy()
                print(f"Found three: {three}")

        elif len(val) == 6: # 0/6/9
            tmp = set()
            for char in val:
                tmp.add(char)
            if four.issubset(tmp):
                nine = tmp.copy()
                print(f"Found nine: {nine}")

    if nine:
        for val in values:
            if len(val) == 5:
                tmp = set()
                for char in val:
                    tmp.add(char)
                if (tmp != three and
                    tmp.issubset(nine)):
                    five = tmp.copy()
                    print(f"Found five: {five}")

    for val in values:
        if len(val) == 5:
            tmp = set()
            for char in val:
                tmp.add(char)
            if (tmp != three and
                tmp != five):
                two = tmp.copy()
                print(f"Found two: {two}")

    if five and nine:
        for val in values:
            if len(val) == 6:
                tmp = set()
                for char in val:
                    tmp.add(char)
                if (tmp != nine and
                    five.issubset(tmp)):
                    six = tmp.copy()
                    print(f"Found six: {six}")

    if five and nine:
        for val in values:
            if len(val) == 6:
                tmp = set()
                for char in val:
                    tmp.add(char)
                if (tmp != nine and
                    not five.issubset(tmp)):
                    zero = tmp.copy()
                    print(f"Found zero: {zero}")


    outputs = line.strip().split("|")[1].split()
    num = ""
    for output in outputs:
        if set(output) == zero:
            num += "0"
        elif set(output) == one:
            num += "1"
        elif set(output) == two:
            num += "2"
        elif set(output) == three:
            num += "3"
        elif set(output) == four:
            num += "4"
        elif set(output) == five:
            num += "5"
        elif set(output) == six:
            num += "6"
        elif set(output) == seven:
            num += "7"
        elif set(output) == eight:
            num += "8"
        elif set(output) == nine:
            num += "9"

    totals.append(num)

print(sum([int(total) for total in totals]))

