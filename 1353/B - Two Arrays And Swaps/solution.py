import sys
 
input = sys.stdin.readline
 
def main():
    n = int(input())
    for _ in range(n):
        a,b = map(int,input().split())
        l_a = list(map(int,input().split()))
        l_b = list(map(int,input().split()))
        l_b.sort(reverse=True)
        l_a.sort()
        for i in range(b):
            if l_a[i] < l_b[i]:
                l_a[i],l_b[i] = l_b[i],l_a[i]
            else:
                break
        print(sum(l_a))
 
if __name__ == "__main__":
    main()