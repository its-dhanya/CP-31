t = int(input())
for _ in range(t):
    a , b , n = map(int , input().split())
    tool = list(map(int , input().split()))
    ans = 0
    for i in tool:
        ans += min(i , a - 1)
    print(ans + b)
