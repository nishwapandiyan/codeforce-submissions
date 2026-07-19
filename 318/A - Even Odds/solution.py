import sys
input = sys.stdin.readline
 
def main():
    n, k = map(int, input().split())
 
    odd = (n + 1) // 2
 
    if k <= odd:
        print(2 * k - 1)
    else:
        print(2 * (k - odd))
 
if __name__ == "__main__":
    main()