t = int(input())
for _ in range(t):
    s = input()
    if s[0] == s[-1]:
        print(s)
    else:
        print(s[0:-1] + s[0])