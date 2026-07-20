import sys
from math import gcd
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int,input().split()))
 
        lst.sort(key=lambda x:x%2)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if gcd(lst[i],2*lst[j]) > 1:
                    ans += 1
        print(ans)
if __name__ == "__main__":
    main()