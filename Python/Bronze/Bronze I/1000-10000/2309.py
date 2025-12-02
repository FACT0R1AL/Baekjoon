import itertools

height = []

for i in range(9):
    height.append(int(input()))

height.sort()
nPr = list(itertools.permutations(height, 7))
max = 0
arr = []

for i in range(len(nPr)):
    if (sum(nPr[i]) > max and sum(nPr[i]) == 100): 
        arr = list(nPr[i])

arr.sort()

for i in range(7):
    print(arr[i])