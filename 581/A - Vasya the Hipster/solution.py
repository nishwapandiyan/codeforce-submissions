import sys
input = sys.stdin.readline
 
def main():
    r,b = map(int,input().split())
    fashion = min(r,b)
    rem = abs(r-b)
    ord = rem // 2
    print(f"{fashion} {ord}")
if __name__ == "__main__":
    main()