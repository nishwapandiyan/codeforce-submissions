import sys
input = sys.stdin.readline
 
def main():
    t = int(input())
 
    for _ in range(t):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
 
        arr.sort()
 
        if sum(arr) == x:
            print("NO")
            continue
 
        s = 0
 
        for i in range(n):
            if s + arr[i] == x:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            s += arr[i]
 
        print("YES")
        print(*arr)
 
if __name__ == "__main__":
    main()