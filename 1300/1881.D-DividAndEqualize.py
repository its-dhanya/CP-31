from collections import defaultdict

def findprimes(num, primefact):
    i = 2
    while i * i <= num:
        while num % i == 0:
            primefact[i] += 1
            num //= i
        i += 1
    if num > 1:
        primefact[num] += 1

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    primefact = defaultdict(int)
    for ele in arr:
        findprimes(ele, primefact)

    valid = True
    for i in primefact:
        if primefact[i] % n:
            print("NO")
            valid = False
            break
    if valid:
        print("YES")
