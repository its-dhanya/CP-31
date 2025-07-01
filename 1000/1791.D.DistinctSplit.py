t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    seen = set()
    pref = [0]*n
    for i, ch in enumerate(s):
        seen.add(ch)
        pref[i] = len(seen)
    seen.clear()
    suff = [0]*n
    for i in range(n-1, -1, -1):
        seen.add(s[i])
        suff[i] = len(seen)
    ans = 0
    for i in range(n-1):
        ans = max(ans, pref[i] + suff[i+1])
    print(ans)
