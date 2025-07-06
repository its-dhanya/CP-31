t = int(input())
for _ in range(t):
    a = input()
    b = input()
    n = len(a)
    m = len(b)
    best = 0
    dp = [0] * (m + 1)
    for i in range(1 , n + 1):
        newdp = [0] * (m + 1)
        for j in range(1 , m + 1):
            if a[i - 1] == b[j - 1]:
                newdp[j] = dp[j - 1] + 1
                best = max(best , newdp[j])
        dp = newdp
    print(n + m - 2 * best)
    