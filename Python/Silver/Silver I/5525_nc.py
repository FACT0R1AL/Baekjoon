import sys

input = sys.stdin.readline

n = int(input().rstrip())

p = "IO"*n + "I"
lengthP = len(p)

length = int(input().rstrip())
string = input().rstrip()

count = 0
i = 0

while i < length - lengthP + 1:
    if string[i:i+lengthP] == p:
        print(string[i:i+lengthP], p)
        count += 1
        i += 1

    i += 1

    # print(i)

print(count)