import sys
 
input = sys.stdin.readline
 
def main():
    n = int(input())
    arr = list(map(int,input().split()))
 
    mn = min(arr)
    mx = max(arr)
 
    if mn == mx:
        print(0,n*(n-1)//2)
    else:
        mx_ct = arr.count(mx)
        mn_ct = arr.count(mn)
        print(mx-mn,mx_ct * mn_ct)
if __name__ == "__main__":
    main()