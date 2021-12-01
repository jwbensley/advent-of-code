with open("input") as f:
    m = [int(line) for line in f]

count = 0
for i in range(2, len(m)-1):
    count += int(
        (m[i] + m[i-1] + m[i-2]) < (m[i+1] + m[i] + m[i-1])
    )

print(count)