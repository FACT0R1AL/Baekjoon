x = int(input())

temp = x
line = 1

while True:
    temp -= line

    if (temp <= 0):
        break
        
    line += 1

for i in range(temp + line):
    if (line % 2 == 0):
        a, b = i+1, line-i
    else:
        a, b = line-i, i+1

print(f"{a}/{b}")