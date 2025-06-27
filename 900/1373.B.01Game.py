t = int(input())
for _ in range(t):
    s = input()
    n0 = s.count('0')
    n1 = s.count('1')
    ans = min(n0 , n1)
    if ans % 2:
        print("DA")
    else:
        print("NET")
    