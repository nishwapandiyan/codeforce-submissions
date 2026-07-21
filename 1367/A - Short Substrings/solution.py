import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ans = ""
        for i in range(0,len(s)-1,2):
            ans += s[i]
        ans += s[-1]
        print(ans)
 
if __name__ == "__main__":
    main()