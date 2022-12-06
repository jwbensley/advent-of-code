for i in range(13, len(open("input").read().strip())):
    if len(set([open("input").read().strip()[i-y] for y in range(0,14)])) == 14: print(i+1); break