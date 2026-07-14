n = int(input())
lst = list(input())
ct = 0
for i in range(n-1):
    if lst[i] == lst[i+1]:
        ct += 1
print(ct)