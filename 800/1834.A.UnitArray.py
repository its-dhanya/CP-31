t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    neg = arr.count(-1)
    ops = 0
    if neg % 2 == 1:
        neg -= 1
        ops += 1
    cursum = n - 2 * neg
    if cursum < 0:
        mops = (-cursum + 1) // 2
        ops += mops
        neg -= mops
    if neg % 2 == 1:
        ops += 1
    print(ops)