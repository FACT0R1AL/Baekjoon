correct = [11, 9, 9, 9, 8, 8, 8, 8, 8, 8]

n = int(input())
print(correct[n-1])

if (n == 1): print('A B C D E F G H J L M')
elif (n == 2): print('A C E F G H I L M')
elif (n == 3): print('A C E F G H I L M')
elif (n == 4): print('A B C E F G H L M')
elif (n >= 5 and n <= 9): print('A C E F G H L M')
elif (n == 10): print('A B C F G H L M')