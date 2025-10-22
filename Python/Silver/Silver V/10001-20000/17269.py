writing = dict()
temp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

for i in range(26):
    writing[chr(i+ord('A'))] = temp[i]

length1, length2 = map(int, input().split())
name1, name2 = input().split()
name = []

i = 0
while True:
    if (i%2): 
        name.append(name2[i//2])
    else: 
        name.append(name1[i//2])

    i+=1

    if (len(name1) <= i//2):
        name.append(name2[i//2:])
        break
    elif (len(name2) <= i//2):
        name.append(name1[i//2:])
        break

name = "".join(name)
love = []
nextLove = []

for i in range(len(name)):
    if (name[i] != " "):
        love.append(writing[name[i]])

while len(love) > 2:
    for i in range(len(love)-1):
        nextLove.append((love[i] + love[i+1])%10)

    #print(nextLove)
    love.clear()
    
    for i in range(len(nextLove)):
        love.append(nextLove[i])

    nextLove.clear()

if (love[0]): print(f"{love[0]}{love[1]}%")
else: print(f"{love[1]}%")
