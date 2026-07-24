import sys
 
input = sys.stdin.readline
 
def main():
    n = int(input())
    arr = list(map(int, input().split()))
 
    mx = max(arr)
 
    # points[i] = total points if we choose number i
    points = [0] * (mx + 1)
 
    for x in arr:
        points[x] += x
 
        # DP array
    dp = [0] * (mx + 1)
 
    dp[0] = 0
    if mx >= 1:
        dp[1] = points[1]
 
    for i in range(2, mx + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
 
    print(dp[mx])
 
if __name__ == "__main__":
    main()