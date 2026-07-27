import sys
 
input = sys.stdin.readline
 
def main():
    s,k = map(str,input().split())
    arr = list(s)
    n = len(s)
    k = int(k)
 
    for i in range(n):
        if k <= 0:
            break
 
        max_idx = i
        for j in range(i+1, min(n, i+1+k)):
            if arr[j] > arr[max_idx]:
                max_idx = j
 
        for j in range(max_idx,i,-1):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            k -= 1
    print(''.join(arr))
 
if __name__ == "__main__":
    main()