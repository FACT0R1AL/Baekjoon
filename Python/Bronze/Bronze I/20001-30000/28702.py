a = input()
b = input()
c = input()

if (a.isdigit()):
    a = int(a) 
    if ((a+3)%3 == 0 and (a+3)%5 == 0): print('FizzBuzz')
    elif ((a+3)%3 == 0): print('Fizz')
    elif ((a+3)%5 == 0): print('Buzz')
    else: print(a+3)
elif (b.isdigit()):
    b = int(b)
    if ((b+2)%3 == 0 and (b+2)%5 == 0): print('FizzBuzz')
    elif ((b+2)%3 == 0): print('Fizz')
    elif ((b+2)%5 == 0): print('Buzz')
    else: print(b+2)
elif (c.isdigit()):
    c = int(c)
    if ((c+1)%3 == 0 and (c+1)%5 == 0): print('FizzBuzz')
    elif ((c+1)%3 == 0): print('Fizz')
    elif ((c+1)%5 == 0): print('Buzz')
    else: print(c+1)