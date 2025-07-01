t = int(input())
for _ in range(t):
    n , k , b , s = map(int , input().split())
    minsum = b * k
    maxsum = b * k + n * (k - 1)
    if s < minsum or s > maxsum:
        print(-1)
        continue
    a = [0] * n
    a[0] = b * k
    rem = s - minsum
    for i in range(n):
        if rem <= 0:
            break
        add = min(k - 1 , rem)
        a[i] += add
        rem -= add
    print(*a)
