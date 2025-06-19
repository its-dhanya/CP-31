import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        i = 1
        while n % i == 0:
            i += 1
        print(i - 1)

if __name__ == "__main__":
    solve()
