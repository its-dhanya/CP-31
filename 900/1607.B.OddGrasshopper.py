t = int(input())
for _ in range(t):
    ini , n = map(int , input().split())
    arr = [0 , -n , 1 , n + 1]
    ind = n % 4
    val = arr[ind]
    if ini % 2:
        print(ini - val)
    else:
        print(ini + val)