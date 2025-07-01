t = int(input())
for _ in range(t):
    s = input().strip()
    c0 = s.count('0')
    c1 = s.count('1')
    ans = 0
    n = len(s)
    for i in range(n):
        if s[i] == '0' and c1:
            c1 -= 1
            ans += 1
        elif s[i] == '1' and c0:
            c0 -= 1
            ans += 1
        else:
            break
    print(n - ans)