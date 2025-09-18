num8 = input()
idx = (len(num8))*3-1
arr = [0 for _ in range(idx)]

for i in range(len(num8)-1, -1, -1):
    if (num8[i] == "0"): arr[idx-2:idx+1] = ['0', '0', '0']
    elif (num8[i] == "1"): arr[idx-2:idx+1] = ['0', '0', '1']
    elif (num8[i] == "2"): arr[idx-2:idx+1] = ['0', '1', '0']
    elif (num8[i] == "3"): arr[idx-2:idx+1] = ['0', '1', '1']
    elif (num8[i] == "4"): arr[idx-2:idx+1] = ['1', '0', '0']
    elif (num8[i] == "5"): arr[idx-2:idx+1] = ['1', '0', '1']
    elif (num8[i] == "6"): arr[idx-2:idx+1] = ['1', '1', '0']
    elif (num8[i] == "7"): arr[idx-2:idx+1] = ['1', '1', '1']
    idx -= 3

print(int(''.join(arr)))