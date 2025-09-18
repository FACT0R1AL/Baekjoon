import math

def is_prime(n):
    if (n == 2): return 1
    if (n % 2 == 0): return 0

    for i in range(3, int(math.isqrt(n))+1, 2):
        if (n % i == 0):
            return 0
    
    return 1

primes = ['2','3','5','7']
odd = ['1','3','5','7','9']
new_primes = []

n = int(input())
start = int('1' + '0' * (n-1))
end = int('9' * n)

if (n >= 2):
    while True:
        for i in range(len(primes)):
            for j in range(len(odd)):
                new_prime = int(primes[i] + odd[j])
                if (is_prime(new_prime)): new_primes.append(str(new_prime))

        primes.clear()

        for i in range(len(new_primes)):
            primes.append(new_primes[i])

        new_primes.clear()
        
        if (len(primes[0]) == n): break

for i in range(len(primes)):
    print(primes[i])