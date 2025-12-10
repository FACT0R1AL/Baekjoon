s = int(input())

plus = 1
count = 0

while plus <= s:
    count += 1
    s -= plus
    plus += 1

print(count)