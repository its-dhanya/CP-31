t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    rem = [(x % k) if (x % k) != 0 else k for x in arr]
    idxs = list(range(n))
    idxs.sort(key=lambda i: -rem[i])
    print(*[i + 1 for i in idxs])
