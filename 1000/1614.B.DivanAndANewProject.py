t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    index = [(freq , i + 1)for i , freq in enumerate(arr)]
    pos = []
    index.sort(reverse = True)
    i = 1
    while len(pos) < n:
        pos.append(i)
        if len(pos) < n:
            pos.append(-i)
        i += 1
    cost = 0
    coords = [0] * (n + 1)
    for j in range(n):
        freq , ind = index[j]
        coords[ind] = pos[j]
        cost += freq * abs(pos[j])
    print(cost * 2)
    print(*coords)

    
