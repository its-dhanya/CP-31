t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    seen = set()
    ans = 0
    for i in s:
        seen.add(i)
        ans += len(seen)
    print(ans)