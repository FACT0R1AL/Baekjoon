T = int(input())
cnt = [0, 0]
fibonacci = [0,1]

for i in range(2,41):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

for _ in range(T):
    n = int(input())
    if (n == 0): print(1, 0)
    elif (n == 1): print(0, 1)
    else:
        print(fibonacci[n-1], fibonacci[n])