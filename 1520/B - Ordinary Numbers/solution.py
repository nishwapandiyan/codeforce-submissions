import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ct = 0
        x = 1
        while x <= n:
            for i in range(1,10):
                if i*x <= n:
                    ct += 1
            x = x*10 + 1
        print(ct)
 
if __name__ == "__main__":
    main()