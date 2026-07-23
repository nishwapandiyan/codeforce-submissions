import sys
 
input = sys.stdin.readline
 
def main():
        n,m = map(int,input().split())
        arr = list(map(int,input().split()))
 
        maxim = 0
        ans = 0
 
        for i in range(n):
              tr = (arr[i] + m - 1) // m
 
              if tr >= maxim:
                    maxim = tr
                    ans = i+1
 
        print(ans)
 
if __name__ == "__main__":
    main()