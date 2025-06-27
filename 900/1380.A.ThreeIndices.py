t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    found = False
    for i in range(1 , n - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            print("YES")
            print(i , i + 1 , i + 2)
            found = True
            break
    if not found:
        print("NO")
