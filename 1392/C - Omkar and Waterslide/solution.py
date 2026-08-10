import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
 
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
 
        ans = 0
 
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                ans += arr[i] - arr[i + 1]
 
        print(ans)
 
 
if __name__ == "__main__":
    main()