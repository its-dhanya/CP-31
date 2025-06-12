t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    two = arr.count(2)
    if two == 0:
        print(1)
        continue
    elif two % 2:
        print(-1)
        continue
    else:
        c = 0
        prod = 1
        total = two * 2
        for i in range(n):
            if arr[i] == 2:
                c += 1
            if c == two//2:
                print(i + 1)
                break

