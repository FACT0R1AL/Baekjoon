K = int(input())
arr = [1 for _ in range(7368788)]        # 0부터 50만번째 소수
arr[0] = arr[1] = 0
primes = []

#50만번째 소수는 7,368,787

for i in range(2, 7368788):
    if (arr[i]):
        primes.append(i)
        
        for j in range(i*i, 7368788, i):
            arr[j] = 0

print(primes[K-1])