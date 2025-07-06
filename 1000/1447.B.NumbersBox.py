t = int(input())
for _ in range(t):
    n , m = map(int , input().split())
    minno = float('inf')
    zero = 0
    neg = 0
    sumi = 0
    for i in range(n):
        row = list(map(int , input().split()))
        for x in row:
            if x < 0:
                neg += 1
            if x == 0:
                zero += 1
            ax = abs(x)
            sumi += ax
            minno = min(minno , ax)
    if zero > 0 or neg % 2 == 0:
        print(sumi)
    else:
        print(sumi - 2 * minno)
