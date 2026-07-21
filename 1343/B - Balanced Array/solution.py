import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n = int(input())
 
    if n % 4 != 0:
        print("NO")
        continue
 
    print("YES")
 
    even = []
    odd = []
 
    even_sum = 0
    odd_sum = 0
 
    for i in range(1, n // 2 + 1):
        even.append(2 * i)
        even_sum += 2 * i
 
    for i in range(1, n // 2):
        odd.append(2 * i - 1)
        odd_sum += 2 * i - 1
 
    odd.append(even_sum - odd_sum)
 
    print(*(even + odd))