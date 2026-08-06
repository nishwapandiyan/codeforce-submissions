import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        x,y = map(int,input().split())
        a,b = map(int,input().split())
        if b >= 2*a:
            print((x+y)*a)
        else:
            print(min(x,y)*b + abs(x-y)*a)    
 
if __name__ == "__main__":
    main()