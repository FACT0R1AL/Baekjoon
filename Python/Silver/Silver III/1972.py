string = ""

while True:
    string = input()

    if (string == "*"): break

    length = len(string)

    Flags = []
    unique = True

    for a in range(length - 2):
        twins = []

        for i in range(length - 1 - a):
            twin = string[i] + string[i+1+a]
            
            if (twin in twins):
                unique = False
                break
                
            else:
                twins.append(twin)


        Flags.append(unique)

    if (False in Flags): print(f"{string} is NOT surprising.")
    else: print(f"{string} is surprising.")