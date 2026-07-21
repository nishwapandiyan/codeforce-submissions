import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
 
        vis = set()
        ok = True
        for i in range(n):
            if i == 0 or s[i] != s[i-1]:
                if s[i] in vis:
                    ok= False
                vis.add(s[i])
        if ok:
            print("YES")
        else:
            print("NO")
 
if __name__ == "__main__":
    main()