t = int(input())
for _ in range(t):
    n , k = map(int , input().split())
    s = input()
    pre = [0] * (n + 1)
    for i in range(1 , n + 1):
        pre[i] = pre[i - 1] + (1 if s[i - 1] == 'W' else 0)
    ans = k
    for l in range(0 , n - k + 1):
        r = l + k
        white = pre[r] - pre[l]
        ans = min(white , ans)
    print(ans)
