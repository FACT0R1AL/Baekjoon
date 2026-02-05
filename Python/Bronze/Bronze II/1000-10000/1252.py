a, b = input().split()

a = list(a)
b = list(b)

a10 = 0
b10 = 0

for i in range(len(a)-1, -1, -1):
    a[i] = int(a[i])
    a10 += a[i] * pow(2, len(a) - i - 1)

for i in range(len(b)-1, -1, -1):
    b[i] = int(b[i])
    b10 += b[i] * pow(2, len(b) - i - 1)

amb = a10 + b10
maxLength = max(len(a), len(b)) * 2
ambBinary = []

i = 0
while maxLength+1 != i:
    power = pow(2, maxLength - i)

    if (amb >= power):
        amb -= power
        ambBinary.append(1)
    else:
        ambBinary.append(0)

    i += 1

    print(maxLength, i)

firstOne = False

finalBinary = []

for i in range(len(ambBinary)):
    if (ambBinary[i] == 1): firstOne = True
    
    if (firstOne):
        finalBinary.append(ambBinary[i])

firstOne = False

for i in range(len(finalBinary)):
    print(finalBinary[i], end="")

if (finalBinary == []):
    print(0)


# 1010101010 000010
