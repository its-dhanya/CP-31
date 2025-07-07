t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    sarr = sorted([val , i] for i , val in enumerate(arr))
    ind = 0
    tot = 0
    ans = [0] * n
    for i in range(n):
        while ind <= i:
            tot += sarr[ind][0]
            ind += 1
        while ind < n and tot >= sarr[ind][0]:
            tot += sarr[ind][0]
            ind += 1
        ans[sarr[i][1]] = ind - 1
    print(*ans)
        
        