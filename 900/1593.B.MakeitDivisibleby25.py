t = int(input())
inf = float("inf")
arr = ["00" , "25" , "50" , "75"]
def getmindeletions(s , t):
    i = len(s) - 1
    ans = 0
    while i >= 0 and s[i] != t[1]:
        i -= 1
        ans += 1
    if i < 0:
        return inf
    i -= 1
    while i >= 0 and s[i] != t[0]:
        i -= 1
        ans += 1
    if i < 0:
        return inf
    else:
        return ans
    
for _ in range(t):
    n = input()
    ans = inf
    for pair in arr:
        ans = min(ans , getmindeletions(n , pair))
    print(ans)
