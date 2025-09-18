def gcd(a, b):
    div1, div2 = b, a%b
    if (div2 != 0):
        return gcd(div1, div2)
    else:
        return div1

def lcm(a, b):
    return int((a*b) / gcd(a, b))

a, b = map(int, input().split())
print(f"{gcd(a,b)}\n{lcm(a,b)}")