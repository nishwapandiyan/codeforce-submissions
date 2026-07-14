n = int(input())
s = input()
a_c = s.count('A')
d_c = s.count('D')
if a_c > d_c:
    print("Anton")
elif a_c < d_c:
    print("Danik")
else:
    print("Friendship")