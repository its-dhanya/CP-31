t = int(input())
for _ in range(t):
    n , k = map(int , input().split())
    arra = list(map(int , input().split()))
    arrb = list(map(int , input().split()))
    ans = 0
    presum = 0
    maxb = arrb[0]
    for i in range(min(n , k)):
        maxb = max(maxb , arrb[i])
        presum += arra[i]
        rep = k - (i + 1)
        ans = max(ans , presum + rep * maxb)
    print(ans)