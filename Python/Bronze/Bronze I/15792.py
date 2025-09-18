from decimal import Decimal, getcontext

a, b = input().split()
a = float(a)
b = int(b)

getcontext().prec = 2000

result = Decimal(str(a)) / Decimal(str(b))

print(format(result, 'f'))