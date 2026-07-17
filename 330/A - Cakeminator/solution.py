r, c = map(int, input().split())
 
grid = []
for _ in range(r):
    grid.append(input())
 
safe_rows = [False] * r
safe_cols = [False] * c
 
for i in range(r):
    if 'S' not in grid[i]:
        safe_rows[i] = True
 
for j in range(c):
    has_strawberry = False
 
    for i in range(r):
        if grid[i][j] == 'S':
            has_strawberry = True
            break
 
    if not has_strawberry:
        safe_cols[j] = True
 
count = 0
 
for i in range(r):
    for j in range(c):
        if safe_rows[i] or safe_cols[j]:
            count += 1
 
print(count)