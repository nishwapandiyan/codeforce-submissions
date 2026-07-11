n = int(input())
X = 0
for _ in range(n):
    cmd = input()
    if '+' in cmd:
        X += 1
    else:
        X -= 1
print(X)