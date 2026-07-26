n, m = map(int, input().split())
 
right = True
 
for i in range(1, n + 1):
 
    if i % 2 == 1:
        print("#" * m)
 
    else:
        if right:
            print("." * (m - 1) + "#")
        else:
            print("#" + "." * (m - 1))
 
        right = not right