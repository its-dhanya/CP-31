import sys
sys.setrecursionlimit(1 << 25)
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    s= input()
    parent = [[] for _ in range(n + 1)]
    for i , p in enumerate(arr , start = 2):
        parent[p].append(i)
    ans = 0
    def dfs(u):
        global ans
        bal = 1 if s[u - 1] == "W" else -1
        for v in parent[u]:
            bal += dfs(v)
        if bal == 0:
            ans += 1
        return bal
    dfs(1)
    print(ans)