import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        
        minA = min(a)
        minB = min(b)
        
        ans = 0
        
        for i in range(n):
            x = a[i] - minA
            y = b[i] - minB
            
            ans += max(x,y)
        print(ans)    
if __name__ == "__main__":
    main()