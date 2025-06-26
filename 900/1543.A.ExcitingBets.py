t = int(input())
for _ in range(t):
    a , b = map(int , input().split())
    if a == b:
        print(0 , 0)
        continue
    g = abs(a-b) 
    print(g, min(a % g , g - a % g))