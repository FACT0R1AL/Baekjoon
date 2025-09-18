sum = 0

for i in range(1, -1, -1):
    string = input()
    if (string == "black"):
        sum += 0*pow(10,i)
    elif (string == "brown"):
        sum += 1*pow(10,i)
    elif (string == "red"):
        sum += 2*pow(10,i)
    elif (string == "orange"):
        sum += 3*pow(10,i)
    elif (string == "yellow"):
        sum += 4*pow(10,i)
    elif (string == "green"):
        sum += 5*pow(10,i)
    elif (string == "blue"):
        sum += 6*pow(10,i)
    elif (string == "violet"):
        sum += 7*pow(10,i)
    elif (string == "grey"):
        sum += 8*pow(10,i)
    elif (string == "white"):
        sum += 9*pow(10,i)

string = input()
if (string == "black"):
    sum *= 1
elif (string == "brown"):
    sum *= pow(10, 1)
elif (string == "red"):
    sum *= pow(10, 2)
elif (string == "orange"):
    sum *= pow(10, 3)
elif (string == "yellow"):
    sum *= pow(10, 4)
elif (string == "green"):
    sum *= pow(10, 5)
elif (string == "blue"):
    sum *= pow(10, 6)
elif (string == "violet"):
    sum *= pow(10, 7)
elif (string == "grey"):
    sum *= pow(10, 8)
elif (string == "white"):
    sum *= pow(10, 9)

print(sum)