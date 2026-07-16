n = int(input())
events = list(map(int,input().split()))
police = 0
untreat = 0
for val in events:
    if val > 0:
        police += val
    if val == -1:
        if police > 0:
            police -= 1
        else:
            untreat += 1
print(untreat)