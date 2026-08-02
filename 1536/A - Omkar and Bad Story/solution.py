t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
 
    if min(arr) < 0:
        print("NO")
        continue
 
    s = set(arr)
 
    changed = True
 
    while changed:
        changed = False
        nums = list(s)
 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                d = abs(nums[i] - nums[j])
 
                if d not in s:
                    s.add(d)
                    changed = True
 
        if len(s) > 300:
            break
 
    if len(s) > 300:
        print("NO")
    else:
        print("YES")
        print(len(s))
        print(*sorted(s))