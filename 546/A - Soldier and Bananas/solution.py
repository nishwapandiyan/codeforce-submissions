lst = list(map(int,input().split()))
c,d,n = lst
t = 0
for i in range(1,n+1):
    t += i*c
if d > t:
    print(0)
else:
    print(t - d)