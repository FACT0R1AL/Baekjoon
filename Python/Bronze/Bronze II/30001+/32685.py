arr = []

for i in range(3):
    value = bin(int(input()))
    if len(value[2:]) <= 3: arr.append('0' *  (4 - len(value[2:])) + value[2:])
    else: arr.append(value[-4:])

number = arr[0] + arr[1] + arr[2]
number = int('0b' + number, 2)

print('0' * (4 - len(str(number))) + str(number))