t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    c0 = arr.count(0)
    c1 = arr.count(1)
    print(c1 * 1 << c0)