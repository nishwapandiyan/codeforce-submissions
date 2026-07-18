import sys
input = sys.stdin.readline
 
def main():
    n = int(input())
    arr = sorted(list(map(int,input().split())))
    print(*arr)
if __name__ == "__main__":
    main()