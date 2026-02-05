string = input()
length = len(string)

JOI = 0
IOI = 0

for i in range(2, length):
    # print(string[i-2:i+1])
    if (string[i-2:i+1] == "JOI"):
        JOI += 1
    elif (string [i-2:i+1] == "IOI"):
        IOI += 1

print(JOI)
print(IOI)