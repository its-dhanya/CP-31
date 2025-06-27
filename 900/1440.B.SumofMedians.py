t = int(input())
for _ in range(t):
    n , k = map(int , input().split())
    arr = list(map(int , input().split()))
    arr.sort()
    m = n // 2
    step = m + 1
    ind = len(arr) - step
    ans = 0
    for _ in range(k):
        ans += arr[ind]
        ind -= step
    print(ans)