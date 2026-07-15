n = int(input())
current = 0
maxim = 0
for _ in range(n):
    a,b = map(int,input().split())
    
    current -= a 
    current += b
    
    maxim = max(maxim,current)
print(maxim)    