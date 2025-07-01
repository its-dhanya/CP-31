t = int(input())
for _ in range(t):
    n = int(input())
    a = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            a = n // i
            break
        i += 1
    print(a , n - a)