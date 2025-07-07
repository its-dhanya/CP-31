t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    currsum = arr[0]
    maxsum = arr[0]
    for i in range(1 , n):
        if arr[i] % 2 != arr[i - 1] % 2:
            currsum = max(currsum + arr[i] , arr[i])
        else:
            currsum = arr[i]
        maxsum = max(currsum , maxsum)
    print(maxsum)