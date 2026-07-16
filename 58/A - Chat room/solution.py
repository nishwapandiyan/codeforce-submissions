s = input()
tr = 'hello'
ptr = 0
for ch in s:
    if ptr < len(tr) and ch == tr[ptr]:
        ptr += 1
if ptr == len(tr):
    print("YES")
else:
    print("NO")