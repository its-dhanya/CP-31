t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    for d in range(1 , 10):
        x = d
        while x <= n:
            c += 1
            x *= 10
    print(c)