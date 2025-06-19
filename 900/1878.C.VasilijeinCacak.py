t = int(input())
for _ in range(t):
    n , k , x = map(int , input().split())
    first=  k * (k + 1) // 2
    last= k * (2 * n - k + 1)
    if first <= x <= last:
        print("YES")
    else:
        print("NO")
    