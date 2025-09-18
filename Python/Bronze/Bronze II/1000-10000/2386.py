while True:
    cnt = 0
    string = input()

    if (string[0] == "#"): break

    for i in range(1, len(string)):
        if (string[i].upper() == string[0].upper()): cnt += 1
    print(string[0], cnt)