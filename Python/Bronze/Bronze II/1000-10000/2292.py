n = int(input())

count = 1
temp = 1


while (temp < n):
    count += 1
    temp += 6 * (count-1)

print(count)