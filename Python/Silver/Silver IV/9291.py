testcase = int(input())

for n in range(1, testcase+1):
    arr = []

    wrongFlag = False
    
    if (n != 1): input()
    
    for i in range(9):
        temp = list(map(int, input().split()))
        arr.append(temp)

    for i in range(9):
        CheckNumber = [False for _ in range(1, 10)]
        if (wrongFlag): break

        for j in range(9):
            if not (CheckNumber[arr[i][j] - 1]):
                CheckNumber[arr[i][j] - 1] = True
            else:
                # print(f"Coordinate : {i} {j}")
                wrongFlag = True
                break

    if (wrongFlag):
        # print("Wrong place in Horizontal line")
        print(f"Case {n}: INCORRECT")
        continue
    
    for j in range(9):
        CheckNumber = [False for _ in range(1, 10)]
        if (wrongFlag): break

        for i in range(9):
            if not (CheckNumber[arr[i][j] - 1]):
                CheckNumber[arr[i][j] - 1] = True
            else:
                # print(f"Coordinate : {i} {j}")
                wrongFlag = True
                break

    if (wrongFlag):
        # print("Wrong place in Vertical line")
        print(f"Case {n}: INCORRECT")
        continue

    for a in range(3):
        for b in range(3):
            CheckNumber = [False for _ in range(1, 10)]
            if (wrongFlag): break

            for j in range(3):
                for k in range(3):
                    if not (CheckNumber[arr[j+b*3][k+a*3] - 1]):
                        CheckNumber[arr[j+b*3][k+a*3] - 1] = True
                    else:
                        # print(f"Coordinate : {i} {j}")
                        wrongFlag = True
                        break

    if (wrongFlag):
        # print("Wrong place in Square")
        print(f"Case {n}: INCORRECT")
        continue
    else:
        print(f"Case {n}: CORRECT")