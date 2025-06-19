t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = 1
    consec = 1
    for i in range(1 , n):
        if s[i - 1] == s[i]:
            consec += 1
            ans = max(ans , consec)
        else:
            consec = 1
    print(ans + 1)