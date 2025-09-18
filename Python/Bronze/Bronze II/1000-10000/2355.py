a, b = map(int, input().split())

if (a > b):
    temp = a
    a = b
    b = temp

print(int((a+b) * (b-a+1) / 2))