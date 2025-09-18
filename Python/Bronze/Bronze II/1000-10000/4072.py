while True:
    arr = list(input().split())
    if (arr[0] == '#' and len(arr) == 1): break

    for i in range(len(arr)):
        lengthWord = len(arr[i])

        for j in range(lengthWord-1, -1, -1):
            print(arr[i][j], end='')
        print(' ', end='')
    
    print('')