import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        arr = list(map(int,input().split()))
        arr.sort(reverse = True)
        
        time = 0
        ans = 0
        for pos in arr:
            if time >= pos:
                break
            time += n-pos
            ans += 1
        print(ans)        
    
 
if __name__ == "__main__":
    main()