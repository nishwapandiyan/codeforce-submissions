import sys
input = sys.stdin.readline
 
def main():
    n = int(input())
    lst = list(map(int,input().split()))
    if 1 in lst:
        print(-1)
    else:
        print(1)
if __name__ == "__main__":
    main()