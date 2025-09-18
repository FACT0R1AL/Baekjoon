import sys

mask = 0
q = int(sys.stdin.readline().rstrip())

for _ in range(q):
    temp = sys.stdin.readline().rstrip()
    cmd, n = '', 0

    if (temp[-1].isdigit()):
        cmd, n = temp.split()
        n = int(n)
    else:
        if (temp[0] == 'a'): cmd = 'all'
        elif (temp[0] == 'e'): cmd = 'empty'

    if cmd == 'add':
        arr[n-1] = 1
    elif cmd == 'remove':
        arr[n-1] = 0
    elif cmd == 'toggle':
        arr[n-1] ^= 1
    elif cmd == 'check':
        sys.stdout.write(str(arr[n-1]) + '\n')
    elif cmd == 'all':
        arr = [1] * 20
    elif cmd == 'empty':
        arr = [0] * 20