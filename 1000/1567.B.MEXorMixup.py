t = int(input())
for _ in range(t):
    a , b = map(int , input().split())
    rem = (a - 1) % 4
    if rem == 0:
        xor = a - 1
    elif rem == 1:
        xor = 1
    elif rem == 2:
        xor = a
    else:
        xor = 0
    if xor == b:
        print(a)
    else:
        y = xor ^ b
        print(a + 1 if y != a else a + 2)