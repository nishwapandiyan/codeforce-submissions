import sys
input = sys.stdin.readline
 
def main():
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
 
    cur = sum(arr[:k])
    minimum = cur
    ans = 0
 
    for i in range(k,n):
        cur = cur - arr[i-k] + arr[i]
 
        if cur < minimum:
            minimum = cur
            ans = i-k+1
    print(ans+1)
if __name__ == "__main__":
    main()