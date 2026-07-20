import sys
 
input = sys.stdin.readline
 
def main():
    n,s = map(int,input().split())
    need = []
    for _ in range(s):
        a,b = map(int,input().split())
        need.append([a,b])
    need.sort()
    ok = True
    for val in need:
        if n > val[0]:
            n += val[1]
        else:
            ok =False
    if ok:
        print("YES")
    else:
        print("NO")
 
if __name__ == "__main__":
    main()