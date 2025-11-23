import sys

input = sys.stdin.readline

listen, see = map(int, input().rstrip().split())
listenA = []
seeA = set()
listenSee = []

for i in range(listen):
    listenA.append(input())

for i in range(see):
    seeA.add(input())

for i in range(listen):
    if (listenA[i] in seeA): listenSee.append(listenA[i])

print(len(listenSee))
listenSee.sort()

for i in range(len(listenSee)):
    print(listenSee[i], end = '')