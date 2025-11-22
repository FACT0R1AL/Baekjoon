word1, word2 = input().split()

lengthA = len(word1)
lengthB = len(word2)

minCount = lengthB

for i in range(lengthB - lengthA + 1):
    count = 0
    temp = word2[i:i+lengthA]

    for j in range(lengthA):
        if (word1[j] != temp[j]): count += 1

    if (count < minCount): minCount = count

print(minCount)