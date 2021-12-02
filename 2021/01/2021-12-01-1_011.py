"""
Lines of code: low
Readability: medium
Efficiency: low

It's only five lines of code, but readability isn't great and this is very
inificient because walk the input file 2n+1 times.
"""

count = 0
for i, val in enumerate(open("input")):
    if int(list(open("input"))[i].strip()) > int(list(open("input"))[i-1].strip()):
        count+= 1
print(count)