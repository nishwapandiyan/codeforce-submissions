num = input()
count = 0
for ch in num:
    if ch == '4' or ch == '7':
        count += 1
count = str(count)
ok = True
for i in count:
    if i != '4' and i != '7':
        ok = False
        break
if ok:
    print("YES")
else:
    print("NO")