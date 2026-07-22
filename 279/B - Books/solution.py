import sys
 
input = sys.stdin.readline
 
def main():
    n,t = map(int,input().split())
    arr = list(map(int,input().split()))
 
    l = 0
    ans = 0
    book_sum = 0
 
    for i in range(n):
        book_sum += arr[i]
 
        while book_sum > t:
            book_sum -= arr[l]
            l += 1
        ans = max(ans,i-l+ 1)
    print(ans)
if __name__ == "__main__":
    main()