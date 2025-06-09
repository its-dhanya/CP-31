t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    ans = 0
    cons = 0
    for i in arr:
        if i == 0:
            cons += 1
            ans = max(ans , cons)
        else:
            cons = 0
    print(ans)

