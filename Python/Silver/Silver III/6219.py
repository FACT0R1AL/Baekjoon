erathos = [1] * 4000001
erathos[0] = erathos[1] = 0

for i in range(2, 4000001):
    if (erathos[i] == 1):
        for j in range(i*i, 4000001, i):
            erathos[j] = 0

a, b, d = map(int, input().split())

count = 0

for i in range(a, b+1):
    if (erathos[i] == 1):
        prime = str(i)

        if (str(d) in prime):
            count += 1

print(count)