n = int(input())
h = list(map(int, input().split()))
 
energy = 0
ans = 0
prev = 0
 
for x in h:
 
    energy += prev - x
 
    if energy < 0:
        ans += -energy
        energy = 0
 
    prev = x
 
print(ans)