n = input()

while (n != '0'):
    count = 0
    for i in n:
        if i == '1': count += 2
        elif i == '0': count += 4
        else: count += 3

    print(count + len(n)+1)

    n = input()