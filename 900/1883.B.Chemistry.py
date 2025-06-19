from collections import Counter
t = int(input())
for _ in range(t):
    n , k = map(int , input().split())
    s = input()
    count = Counter(s)
    odd = 0
    for i in count:
        if count[i] % 2:
            odd += 1
    if odd > k + 1:
        print("NO")
    else:
        print("YES")