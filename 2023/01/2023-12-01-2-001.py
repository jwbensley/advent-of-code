import re;
strings = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
pattern = "(?=(" + "|".join(string for string in strings.keys()) + "))";
print(sum(int(strings[re.findall(pattern, l)[0]] + strings[re.findall(pattern, l)[-1]]) for l in open("input", "r")))

"""
# Working
total = 0
pattern = "(?=(" + "|".join(string for string in strings.keys()) + "))"
for l in open("input", "r"):
    instances = re.findall(pattern, l)
    total += int(strings[instances[0]] + strings[instances[-1]])
print(total)
"""
