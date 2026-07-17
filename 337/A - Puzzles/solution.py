import sys
input = sys.stdin.readline
 
def main():
    n,m = map(int,input().split())
    res = []
    lst = list(map(int,input().split()))
    lst.sort()
    for i in range(m-n+1):
        curr = max(lst[i:n+i]) - min(lst[i:n+i])
        res.append(curr)
    print(min(res))
if __name__ == "__main__":
    main()