import math
t = int(input())
for _ in range(t):
    n , r , b = map(int , input().split())
    consecr = (r // (b + 1))
    rem = r % (b + 1)
    rs = ''
    p = r % b + 1
    for i in range(consecr):
        rs += 'R'
    ans = ''
    for i in range(b + 1):
        if i > 0:
            ans += 'B'
        ans += rs
        if rem > 0:
            ans += 'R'
            rem -= 1
    print(ans)

        