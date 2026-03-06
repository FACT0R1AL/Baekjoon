password = ""
vowels = ['a', 'e', 'i', 'o', 'u']
constants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
alphabets = []
triple = []
double = []

for i in range(26):
    alphabets.append(chr(97+i))

    if (chr(97+i) != 'e' and chr(97+i) != 'o'):
        double.append(chr(97+i)*2)

for i in range(5):
    for j in range(5):
        for k in range(5):
            triple.append(vowels[i]+vowels[j]+vowels[k])

for i in range(21):
    for j in range(21):
        for k in range(21):
            triple.append(constants[i]+constants[j]+constants[k])
    
while True:
    password = input()

    if (password == "end"):
        break

    flag = True
    hasVowel = False

    for i in range(len(password)):
        if (password[i] in vowels):
            hasVowel = True

    if (hasVowel == False):
        print(f"<{password}> is not acceptable.")
        continue

    for i in range(len(password)):
        if (i >= 2 and password[i-2:i+1] in triple):
            #print(password[i-2:i+1])
            print(f"<{password}> is not acceptable.")
            flag = False
            break

        if (i >= 1 and password[i-1:i+1] in double):
            #print(password[i-1:i+1])
            print(f"<{password}> is not acceptable.")
            flag = False
            break

    if (flag and hasVowel == True):
        print(f"<{password}> is acceptable.")