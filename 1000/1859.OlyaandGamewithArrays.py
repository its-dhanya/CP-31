t = int(input())
for _ in range(t):
    n = int(input())
    smin = []
    gmin = float('inf')
    for _ in range(n):
        m = int(input())
        arr = sorted(list(map(int , input().split())))
        gmin = min(gmin , arr[0])
        if m > 1 : smin.append(arr[1])
    ans = gmin + sum(smin) - min(smin)
    print(ans)
