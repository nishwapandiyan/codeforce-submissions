import sys
input = sys.stdin.readline
 
def check(k, n):
    remaining = n
    vasya = 0
 
    while remaining > 0:
 
        take = min(k, remaining)
        vasya += take
        remaining -= take
 
        remaining -= remaining // 10
 
    return vasya * 2 >= n
 
def main():
    n = int(input())
 
    left = 1
    right = n
    ans = n
 
    while left <= right:
        mid = (left + right) // 2
 
        if check(mid, n):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)
 
if __name__ == "__main__":
    main()