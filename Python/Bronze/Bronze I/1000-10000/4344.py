T = int(input())

for _ in range(T):
    cnt = 0
    arr = list(map(int, input().split()))
    avg = sum(arr[1:])/(len(arr)-1)
    
    for i in range(1, arr[0]+1):
        if (arr[i] > avg): 
            cnt += 1
    print(f"{cnt/(len(arr)-1)*100:.3f}%")