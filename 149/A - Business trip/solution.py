import sys
 
input = sys.stdin.readline
 
def main():
    n = int(input())
    months = list(map(int,input().split()))
 
    if n == 0:
        print(0)
    else:
        months.sort(reverse=True)
 
        total = 0
        count = 0
 
        for mo in months:
            total += mo
            count += 1
 
            if total >= n:
                print(count)
                break
        else:
            print(-1)
 
if __name__ == "__main__":
    main()