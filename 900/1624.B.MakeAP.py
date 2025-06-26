t = int(input())
for _ in range(t):
    a , b , c = map(int , input().split())
    flag = False
    y = 2 * b - c
    if y > 0 and y % a == 0:
        m = y // a
        if m >= 1:
            flag = True
    
    if not flag:
        y = a + c
        if y % 2 == 0:
            half = y // 2
            if half > 0 and half % b == 0:
                m = half // b
                if m >= 1:
                    flag = True
    if not flag:
        y = 2* b - a
        if y > 0 and y % c == 0:
            m = y // c
            if m >= 1:
                flag = True
    print("Yes" if flag else "No")