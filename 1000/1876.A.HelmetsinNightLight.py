t = int(input())
for _ in range(t):
    n , p = map(int , input().split())
    numr = list(map(int , input().split()))
    cost = list(map(int , input().split()))
    comb = sorted(zip(cost , numr))
    ans = p
    n -= 1
    for c , no in comb:
        if c > p:
            break
        ans += min(no , n) * c
        n -= min(no , n)
    ans += n * p
    print(ans)
