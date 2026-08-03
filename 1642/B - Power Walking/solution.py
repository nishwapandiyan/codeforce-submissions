import sys
input = sys.stdin.readline
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        
        d = len(set(arr))
        
        for k in range(1,n+1):
            print(max(d,k),end=' ')
if __name__ == "__main__":
    main()    