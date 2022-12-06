for i in range(3, len(open("input").read().strip())):
    if len(set([open("input").read().strip()[i-y] for y in range(0,4)])) == 4: print(i+1); break