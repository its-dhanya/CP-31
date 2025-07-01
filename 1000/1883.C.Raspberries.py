t = int(input())
for _ in range(t):
    n , k = map(int , input().split())
    arr = list(map(int , input().split()))
    if k in {2 , 3 , 5}:
        ans = min((k - i % k) %k for i in arr)
    else:
        mini4 = min((4 - i % 4) %4 for i in arr)
        even = sorted((1 if i % 2 else 0) for i in arr)
        mini2 = even[0] + even[1]
        ans = min(mini4 , mini2)
    print(ans)