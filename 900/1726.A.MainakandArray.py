t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int , input().split()))
    ans = max(a[-1] - min(a), max(a) - a[0])
    for i in range(n):
        ans = max(ans , a[i - 1] - a[i])
    print(ans)