t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0 and n >= 4:
        if n % 6 == 0:
            mini = n // 6
        else:
            mini = n // 6 + 1
        maxi = n // 4
        print(mini, maxi)
    else:
        print(-1)
