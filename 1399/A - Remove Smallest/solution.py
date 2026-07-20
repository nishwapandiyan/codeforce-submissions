import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int,input().split()))
 
        ok = True
        lst.sort()
 
        for i in range(n-1):
            if lst[i+1] - lst[i] >1:
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")
 
if __name__ == "__main__":
    main()