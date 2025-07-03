t = int(input())
for _ in range(t):
    n = int(input())
    x = 1
    while (x << 1) <= n - 1:
        x <<= 1
    ans = list(range(x - 1 , -1 , -1)) + list(range(x , n))
    print(*ans)
    