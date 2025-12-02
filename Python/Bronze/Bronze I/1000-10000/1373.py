num8 = input()
idx = int((len(num8))/3)
if (len(num8)%3 == 0): idx -= 1

arr = [0 for _ in range(idx+1)]

for i in range(len(num8)-1, -1, -3):
    if (num8[max(0, i-2):i+1] == '001' or num8[max(0, i-2):i+1] == '1' or num8[max(0, i-2):i+1] == '01'): arr[idx] = '1'
    elif (num8[max(0, i-2):i+1] == '010' or num8[max(0, i-2):i+1] == '10'): arr[idx] = '2'
    elif (num8[max(0, i-2):i+1] == '011' or num8[max(0, i-2):i+1] == '11'): arr[idx] = '3'
    elif (num8[max(0, i-2):i+1] == '100'): arr[idx] = '4'
    elif (num8[max(0, i-2):i+1] == '101'): arr[idx] = '5'
    elif (num8[max(0, i-2):i+1] == '110'): arr[idx] = '6'
    elif (num8[max(0, i-2):i+1] == '111'): arr[idx] = '7'
    elif (num8[max(0, i-2):i+1] == '000'): arr[idx] = '0'
    idx -= 1

for i in range(len(arr)):
    if (type(arr[i]) == str): print(arr[i], end='')

if (num8 == '0'): print('0')