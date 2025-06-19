t = int(input())
for _ in range(t):
    n , k = map(int , input().split())
    arr = list(map(int , input().split()))
    arr.sort()
    cons = 1
    maxi = 1
    for i in range(1 , n):
        if arr[i] - arr[i - 1] <= k:
            cons += 1
            maxi = max(cons , maxi)
        else:
            cons = 1
    print(n - maxi)

