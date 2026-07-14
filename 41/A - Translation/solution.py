s = input()
t = input()
if s[::-1] == t or s == t[::-1]:
    print("YES")
else:
    print("NO")