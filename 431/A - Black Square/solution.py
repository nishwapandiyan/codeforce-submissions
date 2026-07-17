import sys
input = sys.stdin.readline
 
def main():
    n = list(map(int,input().split()))
    s = input().strip()
    ans = 0
    for i in s:
        ans += n[int(i)-1]
    print(ans)
if __name__ == "__main__":
    main()