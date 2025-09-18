ISBN = input()

idx = ISBN.index('*')
m = int(ISBN[-1])

sum = 0

for i in range(len(ISBN)-1):
    if (ISBN[i].isdigit()):
        sum += (3 if i%2 else 1) * int(ISBN[i])

for i in range(10):
    # print(f"{m}  =  {(10 - (sum + (3 if idx%2 else 1) * i)) % 10} {m == (10 - (sum + (3 if idx%2 else 1) * i)) % 10}")
    if (m == (10 - (sum + (3 if idx%2 else 1) * i)) % 10):
        print(i)
        break
        