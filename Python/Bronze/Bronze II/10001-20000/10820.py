while True:
    try:
        string = input()

        countUp = 0
        countLo = 0
        countSp = 0
        countNum = 0

        for s in string:
            if (s.isupper()): countUp += 1
            if (s.islower()): countLo += 1
            if (s == ' '): countSp += 1
            if (s.isdigit()): countNum += 1

        print(countLo, countUp, countNum, countSp)
    except EOFError:
        break

        