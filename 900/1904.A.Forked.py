t = int(input())
for _ in range(t):
    x , y = map(int , input().split())
    xk , yk = map(int , input().split())
    xq , yq = map(int , input().split())
    king = set()
    queen = set()
    pos = [[-x , -y] , [-y , -x] , [y , -x] , [x , -y] , [-x , y] , [x , y] , [-y , x] , [y , x]]
    for dx , dy in pos:
        king.add((xk + dx , yk + dy))
        queen.add((xq + dx , yq + dy))
    common = king & queen
    print(len(common))
