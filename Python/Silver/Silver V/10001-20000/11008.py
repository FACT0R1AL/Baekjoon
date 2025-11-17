T = int(input())

for _ in range(T):
    word, copy = input().split()
    length = len(word)
    lengthCopy = len(copy)

    count = length
    paste = 0

    i = 0

    while i < length:
        # print(word[i:i+lengthCopy])
        if word[i:i+lengthCopy] == copy:
            word = word[:i] + word[i+lengthCopy:]
            count -= lengthCopy
            paste += 1
            i = -1
            length = len(word)

        i += 1

    print(count + paste)

#bbanbanaaabanabananbanaa bana
#bbanaana bana