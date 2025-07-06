t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    st = []
    ans = 0
    for i in s:
        if i == '(':
            st.append('(')
        else:
            if not st:
                ans += 1
            elif st[-1] == '(':
                st.pop()
    ans += len(st)
    print(ans // 2)