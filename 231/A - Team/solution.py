n = int(input())
lst = []
for _ in range(n):
    v = list(map(int,input().split()))
    lst.append(v)
count = 0
for i in lst:
    if sum(i) >= 2:
        count += 1
print(count)