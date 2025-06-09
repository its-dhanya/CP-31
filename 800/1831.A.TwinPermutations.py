t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    maxi = n + 1
    ans = []
    for i in arr:
        ans.append(maxi - i)
    print(' '.join(map(str , ans)))

