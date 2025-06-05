from bisect import bisect_left
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    validind = []
    ans = 0
    for i in range(1 , n + 1):
        if arr[i - 1] < i:
            cnt = bisect_left(validind , arr[i - 1])
            ans += cnt
            validind.append(i)
    print(ans)

