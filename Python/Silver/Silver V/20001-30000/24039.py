arr = [1 for _ in range(300)]
arr[0] = arr[1] = 0
primes = []
n = int(input())

for i in range(2, 300):
    if (arr[i]):
        primes.append(i)
        
        for j in range(i*i, 300, i):
            arr[j] = 0

for i in range(1, len(primes)):
    mul = primes[i] * primes[i-1]
    if (mul > n): 
        print(mul)
        break