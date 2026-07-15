n = int(input())
home = []
away = []
for _ in range(n):
    a,b = map(int,input().split())
    home.append(a)
    away.append(b)
count = 0    
for i in home:
    for j in away:
        if i == j:
            count += 1
print(count)                