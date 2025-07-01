n , d = map(int , input().split())
arr = list(map(int , input().split()))
arr.sort(reverse = True)
ans = 0
i , j = 0 , n - 1
while i <= j:
    ele = arr[i]
    k = d // ele + 1
    if i + k - 1 <= j:
        ans += 1
        i += 1
        j -= (k - 1)
    else:
        break
print(ans)