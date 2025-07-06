import math
t = int(input())

def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for i in range(3 , r + 1 , 2):
        if n % i == 0:
            return False
    return True

def nextprime(n):
    if n <= 2:
        return 2
    p = n if n % 2 else n + 1
    while not prime(p):
        p += 2
    return p
for _ in range(t):
    d = int(input())
    p = nextprime(d + 1)
    cand1 = p ** 3
    q = nextprime(p + d)
    cand2 = p * q
    print(min(cand1 , cand2))
