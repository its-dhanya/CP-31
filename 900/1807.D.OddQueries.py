t = int(input())
for _ in range(t):
    n , q = map(int , input().split())
    arr = list(map(int , input().split()))
    presum = [0] * (n + 1)
    for i in range(n):
        presum[i + 1] = presum[i] + arr[i]
    total = presum[n]
    for a in range(q):
        l , r , k = map(int , input().split())
        l -= 1
        r -= 1
        segment = presum[r + 1] -presum[l]
        newsum = total - segment + k * (r - l + 1)
        if newsum % 2 : print("YES")
        else : print("NO")
