import sys
 
input = sys.stdin.readline
 
def main():
    n = int(input())
    for _ in range(n):
        win = []
        pl = []
        lst = list(map(int,input().split()))
        s1,s2,s3,s4 = lst
        srt = sorted(lst)
        win.append(srt[-1])
        win.append(srt[-2])
        pl.append( max(s1,s2))
        pl.append( max(s3,s4))
 
        if sorted(win) == sorted(pl):
            print("YES")
        else:
            print("NO")
 
if __name__ == "__main__":
    main()