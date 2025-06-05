mod = 998244353
maxn = 2 * 10 ** 5
fact = [1] * maxn
for i in range(2 , maxn):
    fact[i] = (fact[i - 1] * i) % mod
t = int(input())
for _ in range(t):
    s = input()
    l = 1
    block = 0
    prodblock = 1
    rem = 0
    for i in range(1 , len(s)):
        if s[i] == s[i - 1]:
            l += 1
        else:
            prodblock = (prodblock * l) % mod
            rem += l - 1
            l = 1
    prodblock = (prodblock * l) % mod
    rem += l - 1
    if rem == 0:
        print(0 , 1)
    else:
        res = (prodblock * fact[rem]) % mod
        print(rem , res)

