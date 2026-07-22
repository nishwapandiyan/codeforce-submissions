import sys
from bisect import bisect_left
 
input = sys.stdin.readline
 
def main():
    n = int(input())
    arr = list(map(int, input().split()))
 
    pref = []
    s = 0
    for x in arr:
        s += x
        pref.append(s)
 
    m = int(input())
    queries = list(map(int, input().split()))
 
    for q in queries:
        print(bisect_left(pref, q) + 1)
 
if __name__ == "__main__":
    main()