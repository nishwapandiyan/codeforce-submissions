n = int(input())
xs = ys = zs = 0
for _ in range(n):
    x,y,z = map(int,input().split())
    xs += x
    ys += y
    zs += z
print("YES" if xs == ys == zs == 0 else "NO")