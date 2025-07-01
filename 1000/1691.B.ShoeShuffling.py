t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    p = [0] * n
    i = 0
    flag = True
    while i < n:
        j = i + 1
        while j < n and arr[j] == arr[i]:
            j += 1
        l = j - i
        if l == 1:
            flag = False
            break
        for k in range(i , j):
            if k == j - 1:
                p[k] = i + 1
            else:
                p[k] = k + 2
        i = j
    if not flag:
        print(-1)
    else:
        print(*(p))