import sys
input = sys.stdin.readline
def main():
    n = int(input())
    m=0
    c=0
    for _ in range(n):
        a,b = map(int,input().split())
        if a > b:
            m+=1
        elif a < b:
            c += 1
 
    if m > c:
        print("Mishka")
    elif c > m:
        print("Chris")
    else:
        print("Friendship is magic!^^")      
if __name__ == "__main__":
    main()                