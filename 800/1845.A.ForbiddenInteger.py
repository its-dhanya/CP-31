t = int(input())
for _ in range(t):
    n , k , x = map(int , input().split())
    nums = [i for i in range(1 , k + 1) if i != x]
    if not nums:
        print("NO")
        continue
    i = len(nums) - 1
    ans = []
    while n > 0 and i >= 0:
        while n >= nums[i]:
            n -= nums[i]
            ans.append(nums[i])
        i -= 1
    if n == 0:
        print("YES")
        print(len(ans))
        print(" ".join(map(str , ans)))
    else:
        print("NO")
