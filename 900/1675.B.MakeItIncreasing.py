t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    ans = 0
    flag = True
    for i in range(n - 2 , -1 , -1):
        while arr[i] >= arr[i + 1] and arr[i] > 0:
            arr[i] //= 2
            ans += 1
        if arr[i] == arr[i + 1]:
            print(-1)
            flag = False
            break
    if flag: print(ans)
    


