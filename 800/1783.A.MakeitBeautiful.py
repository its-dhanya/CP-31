from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    if arr[0] == arr[n - 1]:
        print("NO")
        continue
    print("YES")
    arr = [arr[n - 1]] + arr[0 : n - 1]
    print(' '.join(map(str, arr)))


