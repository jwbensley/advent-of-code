with open("input") as f:
    measurements = [int(line) for line in f]

count = 0
for i in range(1, len(measurements)):
    count += int(measurements[i] > measurements[i-1])

print(count)