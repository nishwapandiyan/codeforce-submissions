import sys
import math
 
input = sys.stdin.readline
 
LIMIT = 10**6
 
prime = [True] * (LIMIT + 1)
prime[0] = prime[1] = False
 
for i in range(2, int(LIMIT ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, LIMIT + 1, i):
            prime[j] = False
 
n = int(input())
arr = list(map(int, input().split()))
 
for num in arr:
    root = math.isqrt(num)
 
    if root * root == num and prime[root]:
        print("YES")
    else:
        print("NO")