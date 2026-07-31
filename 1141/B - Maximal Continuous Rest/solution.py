n = int(input())
arr = list(map(int, input().split()))
 
arr = arr + arr
 
cur = 0
ans = 0
 
for x in arr:
    if x == 1:
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 0
 
print(min(ans, n))