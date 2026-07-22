import sys
 
input = sys.stdin.readline
 
def main():
    n = int(input())
    arr = list(map(int,input().split()))
 
    cur = 1
    ans = 1
 
    for i in range(1,n):
        if arr[i] >= arr[i-1]:
            cur += 1
        else:
            cur = 1
        ans = max(ans,cur)
    print(ans)
 
if __name__ == "__main__":
    main()