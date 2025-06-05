from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    bitc = defaultdict(int)
    bitset = []
    for _ in range(n):
        arr = list(map(int , input().split()))
        bits = set()
        p = arr[1:]
        for i in p:
            bits.add(i)
            bitc[i] += 1
        bitset.append(bits)
    
    flag = False
    for bit in bitset:
        rem = True
        for b in bit:
            if bitc[b] == 1:
                rem = False
                break
        if rem:
            flag = True
            break
    print("YES" if flag else "NO")
