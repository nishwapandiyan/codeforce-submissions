import sys
input = sys.stdin.readline
 
def main():
 
    n = int(input())
    l_x = list(map(int,input().split()))
    l_y = list(map(int,input().split()))
 
    c = [x for x in range(1,n+1)]
    d = list(set(l_x[1:]+l_y[1:]))
 
    if d == c:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
 
if __name__ == "__main__":
    main()