from collections import defaultdict
t = int(input())
for _ in range(t):
    n , x , y = map(int , input().split())
    arr = map(int , input().split())
    count = defaultdict(int)
    ans = 0
    for i in arr:
        rx = i % x
        ry = i % y
        wantx = (x - rx) % x
        wanty = ry 
        ans += count[(wantx , wanty)]
        count[(rx , ry)] += 1
    print(ans)
