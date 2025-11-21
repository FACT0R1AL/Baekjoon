x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
y = ['8', '7', '6', '5', '4', '3', '2', '1']

direction = {
    'R' : (1,0),
    'L' : (-1,0),
    'B' : (0,1),
    'T' : (0,-1),
    'RT' : (1,-1),
    'LT' : (-1,-1),
    'RB' : (1,1),
    'LB' : (-1,1) } 

kingPos, stonePos, n = input().split()
n = int(n)

kingPos = [ord(kingPos[0]) - ord('A'), 8-int(kingPos[1])]
stonePos = [ord(stonePos[0]) - ord('A'), 8-int(stonePos[1])]

for i in range(n):
    cmd = input()
    
    kingPos = list(map(sum, zip(kingPos, direction[cmd])))
    if (kingPos[0] < 0 or kingPos[0] > 7 or kingPos[1] < 0 or kingPos[1] > 7): kingPos = list(map(lambda a, b: a-b, kingPos, direction[cmd]))
    if (kingPos == stonePos): 
        stonePos = list(map(sum, zip(stonePos, direction[cmd])))
        if (stonePos[0] < 0 or stonePos[0] > 7 or stonePos[1] < 0 or stonePos[1] > 7):
            kingPos = list(map(lambda a, b: a-b, kingPos, direction[cmd]))
            stonePos = list(map(lambda a, b: a-b, stonePos, direction[cmd]))

    # print(x[kingPos[0]] + y[kingPos[1]], x[stonePos[0]] + y[stonePos[1]])
print(x[kingPos[0]] + y[kingPos[1]] +'\n'+ x[stonePos[0]] + y[stonePos[1]])