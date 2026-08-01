import sys
 
input = sys.stdin.readline
 
def main():
    n,a,b = map(int,input().split())
    s = list(input().strip())
    l= 0
    r = len(s)-1
    ans = 0
 
    while l < r:
        if s[l] == '2' and s[r] == '2':
            if a <= b:
                ans += 2*a
                s[l] = s[r] = '0'
            else:
                ans += 2*b
                s[l] = s[r] = '1'
 
        elif s[l] == '2':
            s[l] = s[r]
            ans += a if s[r] == '0' else b
 
        elif s[r] == '2':
            s[r] = s[l]
            ans += a if s[l] == '0' else b
 
        elif s[l] != s[r]:
            print(-1)
            exit()
        l += 1
        r -= 1
 
    if l == r and s[l] == '2':
        ans += min(a,b)
    print(ans)
 
if __name__ == "__main__":
    main()