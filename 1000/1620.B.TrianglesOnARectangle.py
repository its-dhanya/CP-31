t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    xb = list(map(int, input().split()))[1:] 
    xt = list(map(int, input().split()))[1:]
    yl = list(map(int, input().split()))[1:]
    yr = list(map(int, input().split()))[1:]

    basexb = max(xb) - min(xb)
    areaxb = basexb * h

    basext = max(xt) - min(xt)
    areaxt = basext * h

    baseyl = max(yl) - min(yl)
    areayl = baseyl * w

    baseyr = max(yr) - min(yr)
    areayr = baseyr * w

    ans = max(areaxb, areaxt, areayl, areayr)
    print(ans)
