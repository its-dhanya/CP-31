import sys
from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    maxa = defaultdict(int)
    run = 1
    for i in range(1, n):
        if a[i] == a[i-1]:
            run += 1
        else:
            maxa[a[i-1]] = max(maxa[a[i-1]], run)
            run = 1
    maxa[a[-1]] = max(maxa[a[-1]], run)
    maxb = defaultdict(int)
    run = 1
    for i in range(1, n):
        if b[i] == b[i-1]:
            run += 1
        else:
            maxb[b[i-1]] = max(maxb[b[i-1]], run)
            run = 1
    maxb[b[-1]] = max(maxb[b[-1]], run)
    ans = 0
    for x in set(maxa) | set(maxb):
        ans = max(ans, maxa[x] + maxb[x])
    print(ans)
