import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    minheap = []
    ans = [0] * n
    for k in range(n):
        x = arr[k]
        heapq.heappush(minheap , x)
        while minheap and minheap[0] < len(minheap):
            heapq.heappop(minheap)
        ans[k] = len(minheap)
    print(" ".join(map(str , ans)))
