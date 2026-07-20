import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int,input().split()))
        ans = float('inf')
        lst.sort()
        for i in range(n-1):
            ans = min(ans,lst[i+1] - lst[i])
        print(ans)
 
if __name__ == "__main__":
    main()