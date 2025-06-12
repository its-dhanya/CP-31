t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    par = arr[0] % 2 
    c = 1
    ans = 0
    for i in range(1 , n):
        if arr[i] % 2 == arr[i - 1] % 2:
            ans += 1
    print(ans)
