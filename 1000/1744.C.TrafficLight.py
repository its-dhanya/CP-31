import bisect
t = int(input())
for _ in range(t):
    n , c = map(str , input().split())
    n = int(n)
    color = input()
    if c == 'g':
        print(0)
        continue
    green = [i for i , char in enumerate(color) if char == 'g']
    ans = 0
    for i , char in enumerate(color):
        if char != c:
            continue
        j = bisect.bisect_right(green , i)
        if j < len(green):
            ans = max(ans , green[j] - i)
        else:
            ans = max(ans , (n - i) + green[0])
    print(ans) 