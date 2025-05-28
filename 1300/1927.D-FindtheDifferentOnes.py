t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    q = int(input())

    diff = [n] * n
    for i in range(n - 2 , -1 , -1):
        if arr[i] == arr[i + 1]:
            diff[i] = diff[i + 1]
        else:
            diff[i] = i + 1
    for j in range(q):
        l , r = map(int , input().split())
        l -= 1
        r -= 1
        if diff[l] <= r:
            print(l + 1 , diff[l] + 1)
        else:
            print(-1 , -1)