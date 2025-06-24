import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    gcd = 0
    for i in range(n):
        k = abs(arr[i] - (i + 1))
        gcd = math.gcd(gcd , k)
    print(gcd)

