import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        num = int(input())
        if num % 2020 <= num // 2020:
            print("YES")
        else:
            print("NO")
 
    else:
        "NO"
 
if __name__ == "__main__":
    main()