import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        while n%2 == 0:
            n //= 2
        if n == 1:
            print("NO")
        else:
            print("YES")        
 
if __name__ == "__main__":
    main()