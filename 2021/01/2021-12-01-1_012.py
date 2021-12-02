"""
Lines of code: low
Readability: low
Efficiency: low

It's only one line of code, although squashing a loop into list comprehension
is reducing "lines of code" for the worst possible readability. And this is
very inificient because walk the input file 2n+1 times.
"""

print(sum([1 for i, _ in enumerate(open("input")) if int(list(open("input"))[i].strip()) > int(list(open("input"))[i-1].strip())]))