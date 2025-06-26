from collections import Counter
n = int(input())
for _ in range(n):
    arr , targ = input().split()
    c1 = Counter(arr)
    c2 = Counter(targ)
    i = 0
    for char in arr:
        if i < len(targ) and char == targ[i] and c1[char] == c2[char]:
            i += 1
            c2[char] -= 1
        c1[char] -= 1
    if i == len(targ):
        print("Yes")
    else:
        print("No")
