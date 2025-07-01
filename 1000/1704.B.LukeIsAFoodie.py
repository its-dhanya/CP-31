t = int(input())
for _ in range(t):
    n , x = map(int , input().split())
    arr = list(map(int , input().split()))
    minele = arr[0]
    maxele = arr[0]
    ans = 0
    for i in range(1 , n):
        minele = min(minele , arr[i])
        maxele = max(maxele , arr[i])
        if maxele - minele > 2 * x:
            ans += 1
            minele = maxele = arr[i]
    print(ans)
