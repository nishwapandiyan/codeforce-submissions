s = input()
u_c = 0
l_c = 0
for i in s:
    if i.isupper():
        u_c += 1
    if i.islower():
        l_c += 1
if u_c > l_c:
    print(s.upper())
if u_c < l_c or u_c == l_c:
    print(s.lower())