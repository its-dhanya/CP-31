import sysdata = sys.stdin.read().split()
t = int(data[0])
out = []
idx = 1
def fair(n):
    m = n
    while m:
        d = m % 10
        if d and n % d:
            return False
        m //= 10
    return True

for _ in range(t):
    n = int(data[idx]); idx += 1
    while not fair(n):
        n += 1
    out.append(str(n))
sys.stdout.write("\n".join(out))
