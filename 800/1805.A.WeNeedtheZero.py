t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    x = 0
    for i in arr:
        x ^= i
    if n % 2 == 0:
        if x == 0:
            print(0)
        else:
            print(-1)
    else:
        print(x)

        
