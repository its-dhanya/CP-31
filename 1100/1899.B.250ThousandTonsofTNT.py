t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    presum = [0] * (n + 1)
    presum[0] = 0
    ans = 0
    for i in range(1 , n + 1):
        presum[i] = presum[i - 1] + arr[i - 1]
    for i in range(1 , int(n ** 0.5) + 1):
        if n % i == 0:
            for j in (i , n // i):
                maxi = float('-inf')
                mini = float('inf')
                for k in range(j , n + 1 , j):
                    s = presum[k] - presum[k - j]
                    maxi = max(maxi , s)
                    mini = min(mini , s)
                diff = maxi - mini
                ans = max(ans , diff)
    print(ans)


