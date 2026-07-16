n  = int(input())
lst = list(map(int,input().split()))
ans = [0]*n
for i in range(0,len(lst)):
    ans[lst[i]-1] = i+1
print(*ans)