t = int(input())
for _ in range(t):
    x , k = map(int , input().split())
    c = 0
    l = []
    if x % k:
        print(1)
        print(x)
    else:
        for i in range(1 , x):
            if i % k and x - i % k:
                print(2)
                print(i , x - i)
                break

