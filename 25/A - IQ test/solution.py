n = int(input())
odd = []
even = []
lst = list(map(int,input().split()))
for i in range(len(lst)):
    if lst[i]%2 != 0:
        odd.append(lst[i])
    else:
        even.append(lst[i])
if len(odd) < len(even):
    print(lst.index(odd[0])+1)
else:
    print(lst.index(even[0])+1)