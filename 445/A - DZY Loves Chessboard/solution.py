import sys
 
input = sys.stdin.readline
 
def main():
    n,m = map(int,input().split())
    arr = [list(input().strip()) for _ in range(n)]
 
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '-':
                continue
 
            if (i+j) %2 == 0:
                arr[i][j] = 'B'
            else:
                arr[i][j] = 'W'
    for v in arr:
        print(''.join(v))
 
if __name__ == "__main__":
    main()