t = int(input())
for _ in range(t):
    a , b , c , d = map(int , input().split())
    if a - b < c - d or d < b:
        print(-1)
    else:
        print((d -  b) + (a + (d - b) - c))