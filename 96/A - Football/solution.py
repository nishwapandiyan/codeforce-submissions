n = input()
count = 1
for i in range(1,len(n)):
    if n[i-1] == n[i]:
        count += 1
        if count == 7:
            print("YES")
            break
    else:
        count = 1
else:
    print("NO")