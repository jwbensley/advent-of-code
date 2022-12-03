with open("input", "r") as f:
    lines = f.read().strip().split("\n")
    print(sum(map({k:v for (k,v) in list(map(lambda x: [chr(x), x - 96], range(97, 123))) + list(map(lambda x: [chr(x), x - 38], range(65, 91)))}.get, [list(set(lines[i]).intersection(set(lines[i+1]).intersection(set(lines[i+2]))))[0] for i in range(0, len(lines), 3)])))