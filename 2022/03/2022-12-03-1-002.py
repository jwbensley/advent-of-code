priorities = {}
list(map(lambda x: priorities.update({chr(x): x - 96}), range(97, 123)))
list(map(lambda x: priorities.update({chr(x): x - 38}), range(65, 91)))
with open("input", "r") as f:
    print(sum([priorities[p] for p in [l for line in f.read().split("\n") for l in set(line[:(len(line)//2)].strip()) if l in line[(len(line)//2):].strip()]]))