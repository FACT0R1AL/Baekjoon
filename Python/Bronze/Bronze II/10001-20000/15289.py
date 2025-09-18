R = 31
M = 1234567891

sum = 0

length = int(input())
string = input()

for i, s in enumerate(string):
    sum += (ord(s) - ord('a') + 1) * pow(R, i)

print(sum%M)