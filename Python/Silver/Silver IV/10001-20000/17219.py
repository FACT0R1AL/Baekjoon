import sys

input = sys.stdin.readline

length, find = map(int, input().rstrip().split())

dictionary = dict()

for i in range(length):
    a, b = input().rstrip().split()

    dictionary[a] = b

for i in range(find):
    a = input().rstrip()
    print(dictionary[a])