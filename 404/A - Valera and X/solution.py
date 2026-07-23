import sys
input = sys.stdin.readline
 
def main():
    n = int(input())
    mat = [input().strip() for _ in range(n)]
 
    diag = mat[0][0]
    other = mat[0][1]
 
    if diag == other:
        print("NO")
        exit()
    for i in range(n):
        for j in range(n):
            if i == j or i+j == n-1:
                if mat[i][j] != diag:
                    print("NO")
                    exit()
            else:
                if mat[i][j] != other:
                    print("NO")
                    exit()
    else:
        print("YES")
if __name__ == "__main__":
    main()