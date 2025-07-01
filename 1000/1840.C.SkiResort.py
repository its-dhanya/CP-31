t = int(input())
for _ in range(t):
    n , k , q = map(int , input().split())
    arr = list(map(int , input().split()))
    ans , cnt = 0 , 0
    for i in arr:
        if i <= q:
            cnt += 1
        else:
            if cnt >= k:
                m = cnt - k + 1
                ans += m * (m + 1) // 2
            cnt = 0
    if cnt >= k:
        m = cnt - k + 1
        ans += m * (m + 1) // 2
    print(ans)