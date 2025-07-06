t = int(input())
for _ in range(t):
    a , b = map(int , input().split())
    best = float('inf')
    for i in range(31):
        B =  b + i
        if B < 2:
            continue
        moves = i
        ca = a
        while ca > 0:
            ca //= B
            moves += 1
        best = min(moves, best)
    print(best)


