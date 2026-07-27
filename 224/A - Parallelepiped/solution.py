import sys
import math
 
input = sys.stdin.readline
 
def main():
    ab,bc,ca = map(int,input().split())
 
    abc = round(math.sqrt(ab*bc*ca))
    a = abc//bc
    b = abc//ca
    c = abc//ab
 
    print(4*(a+b+c))
if __name__ == "__main__":
    main()