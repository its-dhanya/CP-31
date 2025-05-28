t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    oddsum = 0
    evensum = 0
    bal = {0 : -1}
    found = False
    for i in range(n):
        if (i + 1)% 2:
            oddsum += arr[i]
        else:
            evensum += arr[i]
        balance = oddsum - evensum
        if balance in bal:
            found = True
            break
        bal.setdefault(balance, i)
    print("Yes" if found else "No")
            

        
