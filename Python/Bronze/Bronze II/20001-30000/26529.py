fibonacci = [0,1]

for i in range(2,47):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

T = int(input())

for _ in range(T):
    n = int(input())
    print(fibonacci[n+1])