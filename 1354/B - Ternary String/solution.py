t = int(input())
 
for _ in range(t):
    s = input().strip()
 
    count = {'1':0, '2':0, '3':0}
 
    left = 0
    ans = float('inf')
 
    for right in range(len(s)):
        count[s[right]] += 1
 
        while count['1'] > 0 and count['2'] > 0 and count['3'] > 0:
            ans = min(ans, right - left + 1)
 
            count[s[left]] -= 1
            left += 1
 
    if ans == float('inf'):
        print(0)
    else:
        print(ans)