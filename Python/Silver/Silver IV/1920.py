def search(n):
    global have
    left = 0
    right = len(have)-1

    while (left <= right):
        mid = (left + right) // 2
        if (have[mid] == n):
            return 1
        elif (have[mid] > n):
            right = mid - 1
        elif (have[mid] < n):
            left = mid + 1

    return 0

n = int(input())
have = list(map(int, input().split()))
have.sort()

m = int(input())
arr = list(map(int, input().split()))

for t in arr:
    print(search(t))