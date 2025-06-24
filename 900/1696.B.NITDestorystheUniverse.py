t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    l , r = 0 , n - 1
    block = 0
    count = 0
    while l < n and arr[l] == 0:
        l += 1
    while r >= 0 and arr[r] == 0:
        r -= 1
    for i in range(l , r + 1):
        if arr[i] != 0 and (i == l or arr[i - 1] == 0):
            block += 1
    print(min(2 ,block))
