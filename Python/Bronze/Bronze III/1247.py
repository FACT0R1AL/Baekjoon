for i in range(3):
    sum = 0
    n = int(input())

    for j in range(n):
        num = int(input())
        sum += num
    
    if (sum > 0): print("+")
    elif (sum < 0): print("-")
    else: print("0")