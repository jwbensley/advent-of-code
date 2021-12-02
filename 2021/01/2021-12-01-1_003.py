"""
Lines of code: low
Readability: low
Efficieny: low

It's only two lines of code, although squashing a loop into list comprehension
is reducing "lines of code" for the worst possible readability. And this is
very inificient because walk the input file 2n+1 times.
"""

count = [1 for i, _ in enumerate(open("input")) if int(list(open("input"))[i].strip()) > int(list(open("input"))[i-1].strip())]
print(sum(count))