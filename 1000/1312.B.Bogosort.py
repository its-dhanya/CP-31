t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int , input().split()))
    s.sort(reverse = True)
    print(*s)