t = int(input())
check = set()
maxi = 10 ** 6
for k in range(2 , 1000 + 1):
    val = 1 + k + k * k
    power = k * k
    while val <= maxi:
        check.add(val)
        power *= k
        val += power
for _ in range(t):
    n = int(input())
    if n in check:
        print("YES")
    else:
        print("NO")
    