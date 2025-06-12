import math

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        found = False
        for i in range(n):
            if found:
                break
            for j in range(i+1, n):
                if math.gcd(a[i], a[j]) <= 2:
                    found = True
                    break
        print("YES" if found else "NO")

if __name__ == "__main__":
    main()