arr = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
string = list(input().split())
result = [chr(ord(string[0][0]) - 32)]

for i in range(1, len(string)):
    if string[i] not in arr:
        result.append(chr(ord(string[i][0]) - 32))

for i in range(len(result)):
    print(result[i], end='')