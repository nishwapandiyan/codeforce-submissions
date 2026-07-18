import sys
input = sys.stdin.readline
def main():
    n = int(input())
    s = input().strip().lower()
    if len(set(s)) == 26:
       print("YES")
    else:
       print("NO")
if __name__ == "__main__":
   main()           