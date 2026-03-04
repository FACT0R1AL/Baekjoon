erathos = [1] * 10000
erathos[0] = erathos[1] = 0

primes = []

for i in range(2, 10000):
    if (erathos[i]):
        primes.append(i)

        for j in range(i, 10000, i):
            erathos[j] = 0

T = int(input())

for i in range(T):
    tnum, happy = map(int, input().split())
    happyPrime = happy
    cases = []

    if (happyPrime not in primes):
        print(f"{tnum} {happyPrime} NO")
        continue

    while True:
        happy = list(str(happy))
        print(happy)
        hap = 0

        for h in happy:
            hap += pow(int(h), 2)

        if (hap == 1):
            print(f"{tnum} {happyPrime} YES")
            break
        elif (hap in cases):
            print(f"{tnum} {happyPrime} NO")
            break
        else:
            cases.append(hap)
            happy = hap