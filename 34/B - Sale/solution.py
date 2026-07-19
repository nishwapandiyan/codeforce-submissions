import sys
 
input = sys.stdin.readline
 
def main():
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    profit = 0
    for i in range(k):
        if arr[i] < 0:
            profit -= arr[i]
    print(profit)
 
if __name__ == "__main__":
    main()