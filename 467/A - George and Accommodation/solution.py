n = int(input())
ct = 0
for _ in range(n):
    m,s = map(int,input().split())
    if s-m >= 2:
        ct += 1
print(ct)