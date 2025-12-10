string = ""

while True:
    line = input()
    if "E-N-D" in line:
        string += line.split("E-N-D")[0]
        break
    string += line + "\n"

count = 0
maxCount = 0

word = ""
maxWord = ""

for s in string:
    if (ord('A') <= ord(s) <= ord('Z') or 
        ord('a') <= ord(s) <= ord('z') or
        ord('-') == ord(s)):
        count += 1
        word += s

    else:
        if (count > maxCount and word != "E-N-D"):
            maxCount = count
            maxWord = word
        
        word = ""
        count = 0

    # print(f"word : {word} / count : {count}")

maxWord = list(maxWord)
for i in range(maxCount):   
    if (ord('A') <= ord(maxWord[i]) <= ord('Z')):
        maxWord[i] = chr(ord(maxWord[i]) + 32)
        # print(maxWord[i])

print(''.join(maxWord))