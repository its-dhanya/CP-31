from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    count = Counter(arr)
    if len(count) == len(arr):
        print("NO")
    else:
        print("YES")
