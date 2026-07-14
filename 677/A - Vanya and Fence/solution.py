n,h = map(int,input().split())
frs = list(map(int,input().split()))
s = 0
for val in frs:
    if val <= h:
        s += 1
    elif val > h:
        s += 2
print(s)