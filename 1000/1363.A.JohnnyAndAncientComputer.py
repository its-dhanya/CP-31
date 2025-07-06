t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    fact = 0
    while b % 2 == 0:
        b //= 2
        fact += 1
    while a % 2 == 0:
        a //= 2
        fact -= 1
    if a != b:
        print(-1)
    else:
        diff = abs(fact)
        ops = diff // 3
        if diff % 3 != 0:
            ops += 1
        print(ops)
