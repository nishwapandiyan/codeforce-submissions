s1 = input().upper()
s2 = input().upper()
s3 = input().upper()
com = s1+s2
if sorted(com) == sorted(s3):
    print("YES")
else:
    print("NO")