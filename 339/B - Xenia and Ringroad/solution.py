n, m = map(int, input().split())
tasks = list(map(int, input().split()))
 
current = 1
ans = 0
 
for x in tasks:
    if x >= current:
        ans += x - current
    else:
        ans += (n - current) + x
    current = x
 
print(ans)