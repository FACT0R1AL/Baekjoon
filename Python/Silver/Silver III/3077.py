n = int(input())
hyeon = list(input().split())
answer = {value: i for i, value in enumerate(list(input().split()))}

count = 0

for i in range(n):
    for j in range(i+1, n):
        if (j-i > 0 and answer[hyeon[j]] - answer[hyeon[i]] > 0): count += 1

print(f"{count}/{int(n * (n-1) / 2)}")