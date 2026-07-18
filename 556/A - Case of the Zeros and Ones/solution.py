import sys
input = sys.stdin.readline
def main():
    n = int(input())
    s = input()
    print(abs(s.count('0') - s.count('1')))
if __name__ == "__main__":
    main()