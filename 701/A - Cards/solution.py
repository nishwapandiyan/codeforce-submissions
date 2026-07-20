import sys
 
input = sys.stdin.readline
 
def main():
    n = int(input())
    arr = list(map(int, input().split()))
 
    target = sum(arr) // (n // 2)
 
    used = [False] * n
 
    for i in range(n):
        if used[i]:
            continue
 
        for j in range(i + 1, n):
            if not used[j] and arr[i] + arr[j] == target:
                print(i + 1, j + 1)
                used[i] = True
                used[j] = True
                break
 
if __name__ == "__main__":
    main()