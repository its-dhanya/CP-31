from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    freq = Counter(arr)
    mocc = max(freq.values())
    ans = 0
    while mocc < n:
        char = min(n - mocc , mocc)
        ans += 1 + char
        mocc += char
    print(ans)
        