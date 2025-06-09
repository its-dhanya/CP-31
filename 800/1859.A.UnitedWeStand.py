from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    count = defaultdict(int)
    for i in range(n):
        count[arr[i]] += 1
    if len(count) == 1:
        print(-1)
    else:
        arr.sort()
        maxele = max(arr)
        maxoc = count[maxele]
        a = arr[:n - maxoc]
        b = arr[n - maxoc:]
        lena = len(a)
        lenb = len(b)
        print(lena,lenb)
        print(" ".join(map(str , a)))
        print(" ".join(map(str , b)))
