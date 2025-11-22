import math

T = int(input())

for _ in range(T):
    n = int(input())
    flag = 0

    if (n == 0 or n == 1): n = 2
    
    if (n == 2): flag = 1
    else:
        while (not flag):
            prime_flag = 1
            for i in range(2, int(math.sqrt(n))+1):
                if (n % i == 0):
                    prime_flag = 0
                    break

            if (prime_flag): flag = 1
            else: n += 1

    print(n)